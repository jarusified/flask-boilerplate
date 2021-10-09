class YourService(object):
    _instance = None

    def __init__(self):
        pass

    def __new__(cls):
        if cls._instance is None:
            print("Creating the YourService object")
            cls._instance = super(YourService, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

    def getJSON(self):
        return {}

    def postJSON(self):
        return {}
