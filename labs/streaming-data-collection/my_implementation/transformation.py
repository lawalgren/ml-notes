import base64
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, _):
    logger.info("Event: %s", json.dumps(event))

    output = []
    for record in event['records']:
        entry = json.loads(base64.b64decode(record['data']).decode())
        logger.info("Entry: %s", json.dumps(entry))
        if entry['results']['dob']['age'] < 21:
            record['result'] = 'Dropped'
            output.append(record)
            continue
        new_entry = base64.b64encode(json.dumps({
            "first_name": entry['results']['name']['first'],
            "last_name": entry['results']['name']['last'],
            "age": entry['results']['dob']['age'],
            "gender": entry['results']['gender'],
            "latitude": entry['results']['location']['coordinates']['latitude'],
            "longitude": entry['results']['location']['coordinates']['longitude']
        }).encode())
        record['data'] = new_entry
        record['result'] = 'Ok'
        output.append(record)
    return {'records': output}
