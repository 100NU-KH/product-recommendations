from django.core.management.base import BaseCommand, CommandError

import csv
from decimal import Decimal
from products.models import Product
from django.conf import settings


class Command(BaseCommand):
    """
        CLI command to populate the product model from
        CSV file present in /data directory in project 
        folder.
    """
    
    help = "Instantiate database with the products from raw data"
    
    product_csvfile_path = settings.STATIC_DATA_URL + "/flipkart_com-ecommerce_sample.csv"
    
    
    def handle(self, *args, **options):
        with open(self.product_csvfile_path, mode='r') as file:
            csvFile = csv.DictReader(file)
            self.stdout.write(
                self.style.SUCCESS("CSV file fetched"),
            )
            self.stdout.write(
                self.style.SUCCESS("Instantiating the product model...")
            )
            try:
                for row in csvFile:
                    product_name = row['product_name']
                    product_image = eval(row['image'])[0] if row['image'] else '' # first image from list
                    description = row['description']
                    category = row['product_category_tree'].split(" >> ")[0].strip('[]"')
                    price = Decimal(row['retail_price'] if row['retail_price'] else 0)
                    
                    Product.objects.update_or_create(
                        name=product_name,
                        defaults={
                            "product_image":product_image,
                            'description':description,
                            'category':category,
                            'price': price
                        }
                    )
                    print(product_name)
                    
            except Exception as e:
                raise CommandError(f"Database initialization for products failed.{e.with_traceback(None)}" )
            self.stdout.write(
                self.style.SUCCESS("Products added to database Successfully")
            )
        return