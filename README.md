# Reserva de Hotel

Esta aplicação contempla a solução do problema Reserva de Hotel:

	Uma rede de hoteis operando em Belo Horizonte deseja oferecer serviços de reserva online.
    Eles possuem três hotéis: The Carlyle, The Plaza e Royal Hotel.
    Cada hotel tem preços diferentes durante a semana e final de semana.
    Existem ainda preços diferenciados para clientes vip.

### Instalação do ambiente

1- O projeto utiliza java 1.7, portanto é precido o download do [jdk7](http://www.oracle.com/technetwork/pt/java/javase/downloads/jdk7-downloads-1880260.html) ou superior.

Adicione o diretório do java nas suas variáveis de ambiente

```bash
export JAVA_HOME=<caminho-para-o-java>
```
2- Clone do github (isso vai criar uma cópia do Reserva de Hotel no seu diretório atual)

```bash
git clone https://github.com/serenafernandes/reserva-hotel.git
```

3- Faça o download do [Gradle](https://services.gradle.org/distributions/gradle-2.10-bin.zip).

Descompacte o arquivo gradle-2.10-bin.zip.
Adicione o local escolhido para o gradle nas variáveis de ambiente como GRADLE_HOME, colocando seu diretório bin no PATH

```bash
export GRADLE_HOME="<caminho-para-o-gradle>"
export PATH="$PATH:$GRADLE_HOME/bin"
```

###Compilar

```bash
gradle build
```
###Rodar os testes

```bash
gradle test
```
