USE legoMastersContestants;

CREATE TABLE Seasons(
	seasonId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	country VARCHAR(3),
	num INT(2),
	team_numbers INT(2),
	premiere DATE,
	finale DATE,
	episodes INT(2)
);

CREATE TABLE Teams
(
	teamID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	teamName VARCHAR(20),
	relationship VARCHAR(20),
	genders VARCHAR(2),
	seasonId INT(2),
	placement INT(2),
	CONSTRAINT FK_Season FOREIGN KEY (seasonId)
	REFERENCES Seasons(seasonID)
);

