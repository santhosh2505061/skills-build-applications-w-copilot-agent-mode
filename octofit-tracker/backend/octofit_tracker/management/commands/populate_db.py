from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=timezone.now().date())
        Activity.objects.create(user=users[4], type='Boxing', duration=50, date=timezone.now().date())
        Activity.objects.create(user=users[5], type='Weightlifting', duration=35, date=timezone.now().date())

        # Create Workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body workout')
        w2 = Workout.objects.create(name='Squats', description='Lower body workout')
        w3 = Workout.objects.create(name='Plank', description='Core workout')
        w1.suggested_for.set([users[0], users[1], users[3]])
        w2.suggested_for.set([users[2], users[4], users[5]])
        w3.suggested_for.set([users[1], users[2], users[5]])

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=250, week=1)
        Leaderboard.objects.create(team=dc, points=200, week=1)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
