import json
print('loading function')

def lambda_handler(event, context):
#1 Parse and query string parametres
	transactionId = event['queryStringParameters']['transactionId']
	transactionType = event['queryStringParameters']['Type']
	transactionAmount= event['queryStringParameters']['Amount']


	print('transactionId' = transactionId)
	print('transactionType' = transactionType)
	print('transactionAmount' = transactionAmount)

#2 construct the  body of the response object
	transactionResponse = {}
	transactionResponse['transactionId']= transactionId
	transactionResponse['Type']= transactionType
	transactionResponse['Amount']= transactionAmount
	transactionResponse['message']= 'Thanks your donations'

#3 Construct help response  object
	ResponseObject = {}
	ResponseObject['statusCode']= 200
	ResponseObject['headers'] ()
	ResponseObject['headers']['Content-Type']= aplication/json
	ResponseObject['body']= json.dumps(transactionResponse) 

#4 Return to response
	return ResponseObject
