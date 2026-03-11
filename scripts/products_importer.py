import pandas as pd
import numpy as np 
from decimal import Decimal

class ProductsImporter:
    def __init__(self):
        k=0

    def load(self):
        df = pd.read_csv("data/amazon.csv")
        pd.set_option('display.max_columns', None) 
        print(df.head(5))

        print(df.columns)

        print(f"The Number of Rows are {df.shape[0]}, and columns are {df.shape[1]}.")

        df = df.drop_duplicates(subset="product_id", keep="first")
        print(f"Rows after removing duplicates: {df.shape[0]}")
        

        df['category'] = df['category'].str.replace('|', ', ')

        df['discounted_price'] = df['discounted_price'].str.replace("₹",'')
        df['discounted_price'] = df['discounted_price'].str.replace(",",'')
        df['discounted_price'] = df['discounted_price'].astype('float64')

        df['actual_price'] = df['actual_price'].str.replace("₹",'')
        df['actual_price'] = df['actual_price'].str.replace(",",'')
        df['actual_price'] = df['actual_price'].astype('float64')

        df['discount_percentage'] = df['discount_percentage'].str.replace('%','').astype('float64')

        df['discount_percentage'] = df['discount_percentage'] / 100

        print(df['rating'].value_counts())

        print(df.query('rating == "|"'))

        df['rating'] = df['rating'].str.replace('|', '3.9').astype('float64')

        print(df.query('rating == "|"'))

        # Changing 'rating_count' Column Data Type

        df['rating_count'] = df['rating_count'].str.replace(',', '').astype('float64')

        df.info()

        products = []

        for _, row in df.iterrows():
            product = {
                "id": row.get("product_id"),
                "name": row.get("product_name"),
                "description": row.get("about_product"),
                "price": Decimal(str(row.get("discounted_price"))),
                "image_url": row.get("img_link"),
                "category": row.get("category"),
                "stock": 100  # stock ficticio
            }

            products.append(product)

        return products

    def loadTest(self):
        products_data = [
            {
                "name": "iPhone 15 Pro Max",
                "description": "El iPhone más avanzado con chip A17 Pro, cámara de 48MP con zoom óptico 5x, y titanio de grado aeroespacial. Incluye Dynamic Island y USB-C.",
                "price": Decimal("1199.99"),
                "image_url": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=500&h=500&fit=crop",
                "category": "Smartphones",
                "stock": 25
            },
            {
                "name": "MacBook Pro 14\" M3",
                "description": "MacBook Pro de 14 pulgadas con chip M3, 8GB de memoria unificada, SSD de 512GB. Perfecto para profesionales creativos y desarrolladores.",
                "price": Decimal("1599.00"),
                "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&h=500&fit=crop",
                "category": "Laptops",
                "stock": 15
            },
            {
                "name": "AirPods Pro (3ª generación)",
                "description": "Audífonos inalámbricos con cancelación activa de ruido, audio espacial personalizado y hasta 6 horas de reproducción.",
                "price": Decimal("249.99"),
                "image_url": "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=500&h=500&fit=crop",
                "category": "Audio",
                "stock": 50
            },
            {
                "name": "Samsung Galaxy S24 Ultra",
                "description": "Smartphone premium con S Pen integrado, cámara de 200MP, pantalla Dynamic AMOLED de 6.8 pulgadas y batería de 5000mAh.",
                "price": Decimal("1299.99"),
                "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&h=500&fit=crop",
                "category": "Smartphones",
                "stock": 20
            },
            {
                "name": "Sony WH-1000XM5",
                "description": "Audífonos over-ear con la mejor cancelación de ruido del mercado, 30 horas de batería y calidad de sonido Hi-Res.",
                "price": Decimal("399.99"),
                "image_url": "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=500&h=500&fit=crop",
                "category": "Audio",
                "stock": 30
            },
            {
                "name": "Dell XPS 13 Plus",
                "description": "Ultrabook premium con procesador Intel Core i7 de 12ª generación, 16GB RAM, SSD 1TB y pantalla InfinityEdge de 13.4 pulgadas.",
                "price": Decimal("1449.00"),
                "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&h=500&fit=crop",
                "category": "Laptops",
                "stock": 12
            },
            {
                "name": "iPad Pro 12.9\" M2",
                "description": "iPad Pro con chip M2, pantalla Liquid Retina XDR de 12.9 pulgadas, compatible con Apple Pencil y Magic Keyboard.",
                "price": Decimal("1099.00"),
                "image_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500&h=500&fit=crop",
                "category": "Tablets",
                "stock": 18
            },
            {
                "name": "Nintendo Switch OLED",
                "description": "Consola híbrida con pantalla OLED de 7 pulgadas, 64GB de almacenamiento interno y dock mejorado con puerto LAN.",
                "price": Decimal("349.99"),
                "image_url": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=500&h=500&fit=crop",
                "category": "Gaming",
                "stock": 35
            },
            {
                "name": "Apple Watch Series 9",
                "description": "Smartwatch con chip S9, pantalla Always-On Retina, GPS, seguimiento de salud avanzado y resistencia al agua hasta 50 metros.",
                "price": Decimal("429.00"),
                "image_url": "https://images.unsplash.com/photo-1579586337278-3f436f25d4d3?w=500&h=500&fit=crop",
                "category": "Smartwatches",
                "stock": 40
            },
            {
                "name": "Canon EOS R6 Mark II",
                "description": "Cámara mirrorless full-frame con sensor de 24.2MP, grabación de video 4K 60p, estabilización de imagen de 8 pasos y enfoque automático dual pixel.",
                "price": Decimal("2499.00"),
                "image_url": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500&h=500&fit=crop",
                "category": "Fotografía",
                "stock": 8
            }
        ]
        return products_data