from django.db import models

# Create your models here.
class Week(models.Model) :
    NOT_PLAYED = "NP"
    IN_PROGRESS = "IP"
    COMPLETED = "CP"
    STATUS_CHOICES = (
        (NOT_PLAYED, "Not Played"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
    )


    weekNumber = models.PositiveIntegerField(primary_key=True)
    weekStatus = models.CharField(max_length=2,
        choices=STATUS_CHOICES,
        default=NOT_PLAYED,
    )

    def __str__(self):
        return str(self.weekNumber)

class Game(models.Model) :
    NOT_PLAYED = "NP"
    IN_PROGRESS = "IP"
    COMPLETED = "CP"
    STATUS_CHOICES = (
        (NOT_PLAYED, "Not Played"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
    )
    NINERS = "49ers"
    BEARS = "Bears"
    BENGALS = "Bengals"
    BILLS = "Bills"
    BRONCOS = "Broncos"
    BROWNS = "Browns"
    BUCS = "Bucs"
    CARDINALS = "Cardinals"
    CHARGERS = "Chargers"
    CHIEFS = "Chiefs"
    COLTS = "Colts"
    COWBOYS = "Cowboys"
    DOLPHINS = "Dolphins"
    EAGLES = "Eagles"
    FALCONS = "Falcons"
    GIANTS = "Giants"
    JAGUARS = "Jaguars"
    JETS = "Jets"
    LIONS = "Lions"
    PACKERS = "Packers"
    PANTHERS = "Panthers"
    PATRIOTS = "Patriots"
    RAIDERS = "Raiders"
    RAMS = "Rams"
    RAVENS = "Ravens"
    REDSKINS = "Redskins"
    SAINTS = "Saints"
    SEAHAWKS = "Seahawks"
    STEELERS = "Steelers"
    TEXANS = "Texans"
    TITANS = "Titans"
    VIKINGS = "Vikings"

    TEAM_CHOICES = (
        (NINERS, "49ers"),
        (BEARS, "Bears"),
        (BENGALS, "Bengals"),
        (BILLS, "Bills"),
        (BRONCOS, "Broncos"),
        (BROWNS, "Browns"),
        (BUCS, "Bucs"),
        (CARDINALS, "Cardinals"),
        (CHARGERS, "Chargers"),
        (CHIEFS, "Chiefs"),
        (COLTS, "Colts"),
        (COWBOYS, "Cowboys"),
        (DOLPHINS, "Dolphins"),
        (EAGLES, "Eagles"),
        (FALCONS, "Falcons"),
        (GIANTS, "Giants"),
        (JAGUARS, "Jaguars"),
        (JETS, "Jets"),
        (LIONS, "Lions"),
        (PACKERS, "Packers"),
        (PANTHERS, "Panthers"),
        (PATRIOTS, "Patriots"),
        (RAIDERS, "Raiders"),
        (RAMS, "Rams"),
        (RAVENS, "Ravens"),
        (REDSKINS, "Redskins"),
        (SAINTS, "Saints"),
        (SEAHAWKS, "Seahawks"),
        (STEELERS, "Steelers"),
        (TEXANS, "Texans"),
        (TITANS, "Titans"),
        (VIKINGS, "Vikings")
    )

    gameNumber = models.PositiveIntegerField(primary_key=True)
    weekNumber = models.ForeignKey('Week', on_delete=models.CASCADE)
    gameStatus = models.CharField(max_length=2,
        choices=STATUS_CHOICES,
        default=NOT_PLAYED,
    )
    homeTeam = models.CharField(max_length=30,
        choices=TEAM_CHOICES,
        default=BRONCOS,
    )
    awayTeam = models.CharField(max_length=30,
        choices=TEAM_CHOICES,
        default=BRONCOS,
    )
    homeScore = models.IntegerField()
    awayScore = models.IntegerField()

    def __str__(self):
        return str(self.gameNumber) + ", home team is " + self.homeTeam
