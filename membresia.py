

from abc import ABC, abstractmethod


# Clase para genera una membresia generica que sera la clase padre de todas as clases de membresia considerando que es la clase abstracta
class Membresia(ABC):
    def __init__(self, correo_suscriptor, numero_tarjeta):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    #Para leer los datos de arriba usamos el decorador property
    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor
    
    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta


# Todos las membresias que seran clases deben poseer la posibiidad de cambiar de suscripcion
    @abstractmethod
    def cambiar_suscripcion(self,nueva_membresia):
        pass
    
## ahora se definen las clases que serán ocupadas por las distintas membresias pero no incluiran la totalidad por ello no se adicionan estos metodos a la clase abstracta

class Cancelable(Membresia):
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
    
class Con_regalo:
    def __init__(self):
        self.dias_regalos = 0

class Control_parental:
    def modificar_control_parental(self):
        pass

class Contenido_offline:
    def incrementar_contenido(self):
        pass

## clase para asegurar dias de regalo usando isinstance, con membresia como objeto.

class Asignador_regalos:
    def asignar_dias(membresia):
        if isinstance(membresia,Familiar) or isinstance(membresia,SinConexion):
            membresia.dias_regalo =7
        elif isinstance(membresia,Pro):
            membresia.dias_regalo = 15

class Gratis(Membresia):
    costo = 0
    dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1,2,3,4]:
            from apoyo_desafio import _crear_nueva_membresia   ## me genraba siempre error al tenerlo arriba y consultando, una solucion era dejar este codigo lo mas cerca de el _crear membresia.
            return _crear_nueva_membresia(self,nueva_membresia)
        else:
            return self
        

class Basico(Cancelable):
    costo =3000
    dispositivos = 2

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [2,3,4]:
            from apoyo_desafio import _crear_nueva_membresia
            return _crear_nueva_membresia(self, nueva_membresia)
        else:
            return self

class Familiar(Cancelable,Con_regalo, Control_parental):
    costo = 5000
    dispositivos = 5
# al heredar muchas clases definimos estas clase para llamarlas con init. 
    def __init__(self, correo_suscriptor, numero_tarjeta):
        Cancelable.__init__(self, correo_suscriptor, numero_tarjeta)
        Con_regalo.__init__(self)

        Asignador_regalos.asignar_dias(self)

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1,3,4]:
            from apoyo_desafio import _crear_nueva_membresia
            return _crear_nueva_membresia(self,nueva_membresia)
        else:
            return self
        
class SinConexion(Cancelable,Con_regalo,Contenido_offline):
    costo = 3500
    dispositivos = 2

    def __init__(self, correo_suscriptor, numero_tarjeta):
        Cancelable.__init__(self, correo_suscriptor, numero_tarjeta)
        Con_regalo.__init__(self)
        Asignador_regalos.asignar_dias(self)

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1,2,4]:
            from apoyo_desafio import _crear_nueva_membresia
            return _crear_nueva_membresia(self,nueva_membresia)
        else:
            return self

class Pro(Cancelable,Con_regalo,Contenido_offline, Control_parental):
    costo = 7000
    dispositivos = 6

    def __init__(self, correo_suscriptor, numero_tarjeta):
        Cancelable.__init__(self, correo_suscriptor, numero_tarjeta)
        Con_regalo.__init__(self)
        Asignador_regalos.asignar_dias(self)

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia in [1, 2, 3]:
            from apoyo_desafio import _crear_nueva_membresia
            return _crear_nueva_membresia(self, nueva_membresia)
        return self
