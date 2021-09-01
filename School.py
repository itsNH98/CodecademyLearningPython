class School:
  def __init__(self, name, level, numberOfStudents):
    self._name = name
    self._level = level
    self._numberOfStudents = numberOfStudents

  @property
  def getName(self):
    return self._name
  
  @property
  def getLevel(self):
    return self._level
  
  @property
  def numberOfStudents(self):
    return self._numberOfStudents
  
  @numberOfStudents.setter
  def setnumberOfStudents(self, new_students):
    self._numberOfStudents = new_students

  def __repr__(self):
    return "A {} school named {} with {} students.".format(self._level, self._name, self._numberOfStudents)


class PrimarySchool(School):
  def __init__(self, name, level, numberOfStudents, pickupPolicy):
    super().__init__(name, 'Primary' , numberOfStudents)
    self._pickupPolicy = pickupPolicy
  
  @property
  def pickupPolicy(self):
    return self._pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self._pickupPolicy)



class HighSchool(School):
  def __init__(self, name, level, numberOfStudents, sportsTeams):
    super().__init__(name, 'High' , numberOfStudents)
    self._sportsTeam = sportsTeams
  
  @property
  def sportsTeams(self):
    return self._sportsTeam

  def __repr__(self):
    parentRepr = super().__repr__()
    teams = ''
    for team in self.sportsTeams:
      teams += (team + ' ')
    return "Sport teams here are " + teams

mySchool = School("High School", "High", 420)
print(mySchool)
print(mySchool.getName)
print(mySchool.getLevel)
mySchool.setnumberOfStudents = 300
print(mySchool.numberOfStudents)

primarySchool = PrimarySchool("Hell", "Primary", 666, "Leave your children to die")
print(primarySchool)
print(primarySchool.getName)
print(primarySchool.getLevel)
print(primarySchool.pickupPolicy)
mySchool.setnumberOfStudents = 300
print(mySchool.numberOfStudents)

HighSchool = HighSchool("Ballin", "High", 999, ['Broncos', 'Ducks', 'Ballers'])
print(HighSchool)
print(HighSchool.getName)
print(HighSchool.getLevel)
print(HighSchool.sportsTeams)
mySchool.setnumberOfStudents = 300
print(mySchool.numberOfStudents)
