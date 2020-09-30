import boto3
from boto3.dynamodb.conditions import Key


def query_trip(trip_id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('local-driverbehavior-trip')
    response = table.query(
        KeyConditionExpression=Key('PK').eq(trip_id)
    )
    print("Items found: ", len(response['Items']))
    return response['Items']


if __name__ == '__main__':
    trip_id = "0d86c38b-76e0-4a52-901c-4b4b9039b3b9"
    print(f"Finding trip {trip_id}")
    trips = query_trip(trip_id)
    for trip in trips:
        # print(trip)
        if 'EYT' in trip.keys():
            print("- summary: ", trip['EYT'], ":", trip['DU'])
        else:
            print(trip['EVT'], ":", trip['SK'])
