from django.core.management.base import BaseCommand
from core.models import Estado, Cidade

class Command(BaseCommand):
    help = 'Importa estados e cidades'

    def handle(self, *args, **kwargs):
        estados = [
            {'nome': 'Tocantins', 'sigla': 'TO'},
            {'nome': 'Bahia', 'sigla': 'BA'},
            {'nome': 'Maranhão', 'sigla': 'MA'},
            {'nome': 'Pará', 'sigla': 'PA'},
            {'nome': 'Piauí', 'sigla': 'PI'},
            {'nome': 'Ceará', 'sigla': 'CE'},
        ]

        cidades = [
            # Tocantins
            {'nome': 'Palmas', 'estado': 'TO', 'is_sede': True, 'lat': -10.2128, 'lng': -48.3603},
            {'nome': 'Paraíso do Tocantins', 'estado': 'TO', 'is_sede': True, 'lat': -10.1750, 'lng': -48.8822},
            {'nome': 'Gurupi', 'estado': 'TO', 'is_sede': False, 'lat': -11.7292, 'lng': -49.0689},
            {'nome': 'Araguaína', 'estado': 'TO', 'is_sede': False, 'lat': -7.1927, 'lng': -48.2048},
            {'nome': 'Porto Nacional', 'estado': 'TO', 'is_sede': False, 'lat': -10.7060, 'lng': -48.4080},
            {'nome': 'Colinas do Tocantins', 'estado': 'TO', 'is_sede': False, 'lat': -8.0578, 'lng': -48.4756},
            {'nome': 'Guaraí', 'estado': 'TO', 'is_sede': False, 'lat': -8.8354, 'lng': -48.5114},
            {'nome': 'Almas', 'estado': 'TO', 'is_sede': False, 'lat': -11.5724, 'lng': -47.1697},
            # Pará
            {'nome': 'Marabá', 'estado': 'PA', 'is_sede': True, 'lat': -5.3814, 'lng': -49.1323},
            # Ceará
            {'nome': 'Fortaleza', 'estado': 'CE', 'is_sede': True, 'lat': -3.7172, 'lng': -38.5433},
            {'nome': 'Horizonte', 'estado': 'CE', 'is_sede': True, 'lat': -4.0985, 'lng': -38.4718},
            # Maranhão
            {'nome': 'Timon', 'estado': 'MA', 'is_sede': True, 'lat': -5.0942, 'lng': -42.8369},
            # Piauí
            {'nome': 'Teresina', 'estado': 'PI', 'is_sede': True, 'lat': -5.0892, 'lng': -42.8016},
            # Bahia
            {'nome': 'Barreiras', 'estado': 'BA', 'is_sede': False, 'lat': -12.1439, 'lng': -44.9968},
        ]

        # Criar estados
        for estado_data in estados:
            Estado.objects.get_or_create(nome=estado_data['nome'], sigla=estado_data['sigla'])
            self.stdout.write(self.style.SUCCESS(f"Estado {estado_data['nome']} criado ou já existe"))

        # Criar cidades
        for cidade_data in cidades:
            estado = Estado.objects.get(sigla=cidade_data['estado'])
            Cidade.objects.get_or_create(
                nome=cidade_data['nome'],
                estado=estado,
                is_sede=cidade_data['is_sede'],
                lat=cidade_data.get('lat'),
                lng=cidade_data.get('lng')
            )
            self.stdout.write(self.style.SUCCESS(f"Cidade {cidade_data['nome']} criada ou já existe"))