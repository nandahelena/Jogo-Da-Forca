# 🎮 Jogo da Forca 

Um simples jogo da forca jogável via terminal, feito em Python!  
O jogador precisa adivinhar a palavra secreta, letra por letra, antes que suas tentativas acabem.

---

## 📌 Como funciona

1. O jogo sorteia aleatoriamente uma palavra de um arquivo `palavras.txt`.
2. O jogador tem **6 tentativas** para acertar todas as letras.
3. A cada rodada, o jogador:
   - Visualiza as letras já tentadas.
   - Vê as letras acertadas no lugar certo e os espaços restantes.
4. Se errar, perde uma tentativa.
5. O jogo valida se a entrada:
   - Contém **apenas uma letra**.
   - É um caractere alfabético (A-Z).

---

## 📦 Como executar

1. Certifique-se de ter o Python instalado.
2. Salve o código em um arquivo `.py`.
3. Execute pelo terminal:
```bash
python nome_do_arquivo.py
```

---

## 📂 Sobre o arquivo de palavras

- Ao iniciar, o código lê um arquivo `palavras.txt` com algumas palavras:
  ```
  ESCOLA
  CASA
  COMPUTADOR
  PYTHON
  BICICLETA
  ...
  ```
- Você pode editar esse arquivo para adicionar suas próprias palavras.

---

## ✨ Funcionalidades

- Sorteio de palavra aleatória.
- Sistema de tentativas limitadas.
- Validação de entrada (apenas uma letra e caractere alfabético).
- Exibição de letras já tentadas.
- Atualização dinâmica da palavra oculta.

---

## 📌 Pré-requisitos

- Python 3.x

---

## 📖 Exemplo de execução

```
Bem-vindo ao Jogo da Forca!

Palavra: _ _ _ _ _ _ _ _ _ _

Tentativas restantes: 6
Letras tentadas: Nenhuma

Digite uma letra:
```

---

## 📃 Licença

Projeto feito para fins de aprendizado e prática em Python.
