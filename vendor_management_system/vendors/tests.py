from django.test import TestCase
from .models import Vendor



class VendorTestCase(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name = 'Jithin RS',
            contact_details = 'Some contact details here',
            address = 'Jalaja bhavan anad po nedumangad',

        )
    def test_vendor_creation(self):
        self.assertEqual(self.vendor.name, 'Jithin RS')
        self.assertEqual(self.vendor.contact_details, 'Some contact details here')
        self.assertEqual(self.vendor.address, 'Jalaja bhavan anad po nedumangad')