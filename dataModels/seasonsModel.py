import re

class Seasons:
    def __init__(self, country, num, team_numbers, premiere, finale, episodes):
        self.country = self.__checkString(3, country)
        self.num = self.__checkInt(num, 2)
        self.team_numbers = self.__checkInt(team_numbers, 2)
        self.premiere = premiere
        self.finale = finale
        self.episodes = self.__checkInt(episodes, 2)

    def __checkString(self, size : int, word):
        if len(word) > size:
            wordError = "Words should be {} or smaller".format(size)
            self.__errorMessage(wordError)
            return None
        
        return word

    def __checkInt(self, num, maxBase):
        if type(num) != int:
            self.__errorMessage("Type in an integer")
            return None

        if num >= 10**maxBase:
            numSize = "Integer exceeds size constraint; has to be < {}".format(10**maxBase)
            self.__errorMessage(numSize)
            return None

        return num

    def __checkDate(self, date : str):
        date = date.strip(" ")
        if date == "":
            return None

        x = re.match("[2][0][1?2][0-9][-][0?1][0-9][-][0?1][0-9]", date)
        return date

def checkDate(date : str):
    date = date.strip(" ")

    if date == "":
        return None

    valid = re.match("(20[1-9][0-9])-(0[1-9]|1[0-2])-(0[0-9]|[12][0-9]|[3][0-1])", date)

    if valid is None:
        return valid

    return date
