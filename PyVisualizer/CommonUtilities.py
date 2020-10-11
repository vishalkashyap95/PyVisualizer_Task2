import gspread


class CommonUtilities:
    connectedClientObj = None
    isConnectionSuccessful = False

    def connectAndAutorizeToSeriveAccount(self):
        """
        This method will connect to google service account which is configured in ser_account.json file.
        If successfully connected the it will initialize 'connectedClientObj' variable and set 'isConnectionSuccessful' variable to True
        """
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        try:
            # creds = ServiceAccountCredentials.from_json_keyfile_name("new_cred.json", scope)
            # self.client = gspread.authorize(creds)
            self.connectedClientObj = gspread.service_account("./service_account.json", scopes=scope)
            if type(self.connectedClientObj) is gspread.client.Client:
                self.isConnectionSuccessful = True
                print("Successfully Authorized and Connected to Google Service Account. :)")
            else:
                print("Failed to connect and authorize to service account.")
        except Exception as e:
            print("Exception caught in Connecting and Authorizing Google Service Account : ", e)


    def read_google_sheet(self, sGoogleSheetFileName, sWorkSheetName):
        """
        This method is used to read the google sheet file and worksheet inside it
        :param sGoogleSheetFileName: Accepts Google sheet file name
        :param sWorkSheetName: Accepts what worksheet needs to accessed from the file
        :return: Read the specified sheet and Returns the object of that sheet
        """
        if self.isConnectionSuccessful:
            # print("Successfully Authorized and Connected to Google Service Account. :)")

            # An empty string counts as False, variable with a value in it count as True
            if sGoogleSheetFileName and sWorkSheetName:
                try:
                    sheets = self.connectedClientObj.open(sGoogleSheetFileName)
                    return sheets.worksheet(sWorkSheetName)
                except:
                    raise Exception("Exception caught in reading the GoogleSheetFile/Worksheet.")
            else:
                raise ValueError("Parameter value cannot be empty.")
        else:
            raise Exception("FAILED to authorize to google service account.")
