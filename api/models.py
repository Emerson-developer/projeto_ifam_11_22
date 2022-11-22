from django.db import models
class Regiao(models.Model):
    
    lugar = models.CharField(
    db_column='tx_lugar',
    max_length=15,
    verbose_name='Lugar',
    default="Kanto"
    )
    
    def __str__(self):
        return self.lugar
    
    class Meta:
        managed = True
        db_table = 'Regiao'
        verbose_name = 'Regiao'
        verbose_name_plural = 'Regioes'

class Pokemon(models.Model):
    class Tipo(models.TextChoices):
        AGUA = 'Agua', 'Agua'
        FOGO = 'Fogo', 'Fogo'
        PLANTA = 'Planta', 'Planta'
        ELETRICO = 'Eletrico', 'Eletrico'

    class Sexo(models.TextChoices):
        Macho = 'Macho', 'Macho'
        Femea = 'Femea', 'Femea'

    nome = models.CharField(
        db_column='tx_name',
        max_length=36,
        verbose_name='Nome'
    )
    altura = models.DecimalField(
        db_column='nb_altura',
        max_digits=3,
        decimal_places=2,
        verbose_name='Altura'
    )
    tipo = models.CharField(
        db_column='cs_tipo',
        max_length=16,
        null=False,
        blank=False,
        choices=Tipo.choices,
        verbose_name='Tipo'
    )
    peso = models.DecimalField(
        db_column='nb_peso',
        max_digits=4,
        decimal_places=2,
        verbose_name='Peso'

    )
    sexo = models.CharField(
        db_column='cs_sexo',
        max_length=5,
        null=False,
        blank=False,
        choices=Sexo.choices,
        verbose_name='Sexo'
    )
    
    regiao = models.ForeignKey(
        Regiao,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'pokemon'
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemons'        


class Treinador(models.Model):
    class Sexo(models.TextChoices):
        MASCULINO = 'Masculino', 'Masculino'
        FEMININO = 'Feminno', 'Femino'

    nome = models.CharField(
        db_column='tx_name',
        max_length=36,
        verbose_name='Nome'
    )
    altura = models.DecimalField(
        db_column='nb_altura',
        max_digits=3,
        decimal_places=2,
        verbose_name='Altura'
    )
    idade = models.IntegerField(
        db_column='nb_idade',
        verbose_name='Idade'
    )
    sexo = models.CharField(
        db_column='cs_sexo',
        max_length=16,
        null=False,
        blank=False,
        choices=Sexo.choices,
        verbose_name='Sexo'
    )
    
    regiao = models.ForeignKey(
        Regiao,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        managed = True
        db_table = 'Treinador'
        verbose_name = 'Treinador'
        verbose_name_plural = 'Treinadores'

class Pokebola(models.Model):
    
    captura = models.CharField(
        db_column='tx_captura',
        max_length=10,
        verbose_name='Captura',
        default="Red"
    )
    
    def __str__(self):
     return self.captura
    
    class Meta:
        managed = True
        db_table = 'Pokebola'
        verbose_name = 'Pokebola'
        verbose_name_plural = 'Pokebolas'



class Pool(models.Model):

    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,

    )
    treinador = models.ForeignKey(
        Treinador,
        on_delete=models.CASCADE
    )

    pokebola = models.ForeignKey(
        Pokebola,
        on_delete=models.CASCADE,
        null=True
    )