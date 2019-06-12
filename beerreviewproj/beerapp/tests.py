from django.test import TestCase
from .models import BeerType, Beer, Review
from .views import index, gettypes, getbeers
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class BeerTypeTest(TestCase):
   def test_string(self):
       type=BeerType(typename="Sour")
       self.assertEqual(str(type), type.typename)

   def test_table(self):
       self.assertEqual(str(BeertType._meta.db_table), 'beertype')

class BeerTest(TestCase):
   def setup(self):
       type = BeerType(typename='Lager')
       beer=Beer(beername='Budweiser', beertype=type, beerprice='5.99')
       return beer
   def test_string(self):
       prod = self.setup()
       self.assertEqual(str(prod), prod.beername)
  
   def test_discount(self):
       prod=self.setup()
       self.assertEqual(prod.memberdiscount(), 25.00)

   def test_type(self):
       prod=self.setup()
       self.assertEqual(str(prod.beertype), 'lager')

   def test_table(self):
       self.assertEqual(str(Beer._meta.db_table), 'beer')

class ReviewTest(TestCase):
   def test_string(self):
       rev=Review(reviewtitle="test review")
       self.assertEqual(str(rev), rev.reviewtitle)

   def test_table(self):
       self.assertEqual(str(Review._meta.db_table), 'review')

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetProductsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('beers'))
       self.assertEqual(response.status_code, 200)
