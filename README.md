# Python_requests
Pequenos trechos de código para obter dados (Informações de filmes, cotação de moeda, Clima) utilizando a lib requests do Python

## Instalação:
A unica instalação necessária é a biblioteca <strong>requests<strong>

Você pode adiciona-la ao seu projeto com o seguinte comando

```pip install requests```

lembrando que o pip usará a versão padrão do seu sistema. Caso sejá o Python2 e você quiser instalar com o python3, basta o seguinte comando:

```pip3 install requests```

## Utilizando Virtualenv:

Quando você trabalha com Python é interessante utilizar uma máquina virtual para gerir suas dependencias, assim um projeto que usa dependencias específicas não tera confronto com versões diferentes das mesmas, já que a virtualenv as mantem isoladas do resto do sistema.

Para instalar siga os passos abaixo:

```pip install virtualenv```
ou
```pip3 install virtualenv```

```virtualenv <nome para a env> ```

Depois ative e comece a trabalhar

No Windows:

```cd <nome da env>/scripts```

```activate.bat ```

No Linux e MacOS:
```cd <nome da env>/bin```

```source ./activate```

Lembre-se de ativar sempre que quiser programar e verificar se o interprete Python da sua IDE esta usando a env ;)

### Obs: para a colsulta ao clima é necessaria uma biblioteca chamada googletrans, veja como instalar e utilizar no link abaixo:
-> https://evaldowolkers.wordpress.com/2018/12/12/traducao-de-texto-com-python-e-googletrans/ 

