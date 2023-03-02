class Teams:
    def __init__(self, teamName, relationship, genders, seasonId, placement):
        self.teamName = self.__checkString(20, teamName)
        self.relationship = self.__checkString(20, relationship)
        self.genders = self.__checkGenders(genders)
        self.seasonId = self.__checkInt(seasonId, 100)
        self.placement = self.__checkInt(placement, 100)

    def __checkString(self, size : int, word):
        if len(word) > size:
            return None

        return word

    def __checkInt(self, num, maxNum):
        if type(num) != int or num >= maxNum:
            return -1 

        return num

    def __checkGenders(self, ratio : str):
        if len(ratio) != 2:
            return '??'

        return ratio
