
import azure.functions as func
import logging
#from fastapi.encoders import jsonable_encoder
from Task import invoke_Crew
import json

from EmailHelper import send_email


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    logging.info('Python HTTP trigger function processed a request.')
    logging.info('processscrapper : Started')
    try:
        data = req.get_json()
        logging.info(data)
        logging.info("---CREWAI Started---")
        crew_output=invoke_Crew(data)
        logging.info("---CREWAI End---")

        if data.get('isReddit') == True:
            send_email( 'Reddit: Customer Feedback Summary', crew_output)

        if data.get('isGooglePlayStore') == True:
            send_email( 'Google Play: Customer Feedback Summary', crew_output)
        
        user_encoded = str(crew_output)
        logging.info('processscrapper : Ended')

        return func.HttpResponse(json.dumps(user_encoded),
            mimetype="application/json")

    except Exception as e:
        return func.HttpResponse({"error": str(e)},status_code= 500)
