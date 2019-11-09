class Date:
    def date(self):
        import datetime

        dt_now = datetime.datetime.now()
        
        return dt_now.strftime('%Y_%m_%d_%H:%M')