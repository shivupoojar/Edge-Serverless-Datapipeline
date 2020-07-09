def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    
	video=req.data
	print(video)
	req='200'
	
    return req
