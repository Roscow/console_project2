from django.db import models
from django.utils import timezone


#choices_list
list_alma_mater = (('0','Ninguna'),('01','??'),('1','U de Chile'),('2','U de Santiago'),
('3','U de Valparaiso'),('4','U de Antofagasta'),
('5','U de la Serena'),('6','U de Bío-bio'),('7','U de la Frontera'),
('8','U de Magallanes'),('9','U de Talca'),('10','U de Atacama'),
('11','U de Tarapacá'),('12','U Arturo Prat'),('13','UMCE'),
('14','UPACE'),('15','U de los lagos'),('16','UTEM'),
('17','U de Ohiggins'),('18','U de Aysen'),
('19','PUC'),('20','U de Concepcion'),('21','U tecnica Federico Santa maria'),
('22','PUCV'),('23','U Austral'),('24','U Catolica del norte'),('25','U catolica del Maule'),
('26','U catolica de la Santisima Concepcion'),('27','U catolica de temuco'),
('28','U Gabriela Mostral'),('29','U Finis Terrae'),('30','U Diego Portales'),
('31','U Central'),('32','U Bolivariana'),('33','U Pedro de Valdivia'),('34','U mayor'),
('35','U santo tomas'),('36','U la Republica'),('37','U sek'),('38','UDLA'),
('39','U Andres Bello'),('40','U de Viña del mar'),('41','U adolfo Ibañez'),('42','UNIAC'),
('43','UCINF'),('44','U Autonoma'),('45','U de los Andes'),('46','U adventista'),
('47','U San Sebastian'),('48','ARCIS'),('49','U cardenal raul silva henriquez'),
('50','U del Desarrollo'),('51','U de Aconcagua'),('52','U del Pacifico'),('53','U los leones'),
('54','Bernardo Ohiggins'),('55','INACAP'),('56','U Miguel de Cervantes'),('57','U alberto Hurtado'),
('58','IP libertador de los Andes'),('59','Duoc UC'),('60','Esucomex'),('61','AIEP'),
('62','Arcos'),('63','ENAC'),('64','ICEL'),('65','Manpower'))

list_lenguajes = (('0','??'),('1','Assembly'),('1,5','C'),
('2','C++'),('3','C#'),('4','Cobol'),('5','Delphi'),('6','F'),('7','F#'),
('8','Fortran'),('9','Haskell'),('10','Java'),('11','Javascript'),('12','Lisp'),
('13','MATLAB'),('14','Objective-C'),('15','Pascal'),('16','Perl'),('17','PHP'),
('18','PL/sql'),('19','PowerShell'),('20','Prolog'),('21','Python'),('22','Ruby'),
('23','swift'),('24','T-sql'),('25','Visual Basic'))    






class Programador(models.Model):
    nombre = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    correo =models.CharField(max_length=200)
    bio =  models.TextField()
    alma_mater = models.CharField(max_length=200, choices= list_alma_mater)
    avatar = models.ImageField(null=True, upload_to='albums/images/')

    def __str__(self):
        #llamar el nombre desde nombre(auth.user)
        return self.correo

class Proyecto(models.Model):
    autor = models.ForeignKey('Programador', on_delete=models.CASCADE)
    estado_post = models.CharField(max_length=200)
    link_descarga = models.CharField(max_length=200)
    lenguaje = models.CharField(max_length=200, choices= list_lenguajes)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.titulo   