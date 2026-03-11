#!/usr/bin/env python3
"""
Script para poblar la base de datos con productos reales
"""
import sys
import os

from products_importer import ProductsImporter

# Agregar el directorio raíz al path para importar módulos de la app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.product import Product
from decimal import Decimal

def create_real_products():
    """Crear productos reales en la base de datos"""
    products_importer= ProductsImporter()    
    products_data = products_importer.load()    
    db = SessionLocal()
    try:
        # Eliminar productos existentes para empezar limpio
        db.query(Product).delete()
        db.commit()
        
        print("🗑️  Productos existentes eliminados")
        
        # Crear nuevos productos
        products_created = []
        for product_data in products_data:
            product = Product(**product_data)
            db.add(product)
            products_created.append(product_data["name"])
        
        db.commit()
        
        print(f"✅ {len(products_created)} productos creados exitosamente:")
        for i, name in enumerate(products_created, 1):
            print(f"   {i}. {name}")
        
        # Verificar que se crearon correctamente
        count = db.query(Product).count()
        print(f"\n📊 Total de productos en la base de datos: {count}")
        
    except Exception as e:
        print(f"❌ Error al crear productos: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    """Función principal para poblar la base de datos"""
    print("🚀 Iniciando creación de productos reales...")
    create_real_products()
    print("🎉 ¡Proceso completado!")

if __name__ == "__main__":
    main()