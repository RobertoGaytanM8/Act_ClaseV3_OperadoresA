print("Act 9 Clases v2")
print("Roberto Gaytan --- Mat:22308051281202")


# ZONA DE CLASES

class Operadores1202:
    # ZONA DE FUNCIONES
    def suma1202(self,R,G):
        s1202=R+G
        print(f"La suma de {R} + {G} es igual a {s1202}")

    def resta1202(self,R,G):
        r1202=R-G
        print(f"La resta de {R} - {G} es igual a {r1202}")

    def mult1202(self,R,G):
        m1202=R*G
        print(f"La multiplicacion de {R} x {G} es igual a {m1202}")

    def div1202(self,R,G):
        d1202=R/G
        print(f"La divsion de {R} / {G} es igual a {d1202}")
    
    def mod1202(self,R,G):
        md1202=R%G
        print(f"El modulo de {R} % {G} es igual a {md1202}")

    def expo1202(self,R,G):
        ex1202=R*G
        print(f"El exponente de {R} ** {G} es igual a {ex1202}")

    def cos1202(self,R,G):
        cs1202=R//G
        print(f"El cociente de {R} // {G} es igual a {cs1202}")  


# ZONA DE CREACION DEL OBJETO
operaberto= Operadores1202()


# ZONA DE USO DE OBJETOS
print("")
print("***FUNCION SUMA***")
operaberto.suma1202(5,4)
print("")
print("***FUNCION RESTA***")
operaberto.resta1202(10,6)
print("")
print("***FUNCION MULTIPLICACION***")
operaberto.mult1202(8,9)
print("")
print("***FUNCION DIVISION***")
operaberto.div1202(24,4)
print("")
print("***FUNCION MODULO***")
operaberto.mod1202(2,6)
print("")
print("***FUNCION EXPONENTE***")
operaberto.expo1202(3,3)
print("")
print("***FUNCION COCIENTE***")
operaberto.cos1202(25,2)