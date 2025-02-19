# Fire Detection using YOLO

Este projeto implementa um sistema de detecção de fogo utilizando a biblioteca YOLO da Ultralytics. O modelo é treinado para identificar chamas em tempo real através de uma webcam.

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- OpenCV
- Ultralytics (YOLOv8)
- NumPy

## 📂 Estrutura do Projeto
```
fire-detection/
│── datasets/                # Diretório contendo os dados de treinamento
│── runs/                    # Diretório onde os pesos treinados serão salvos
│── train.py                 # Script para treinar o modelo
│── detect.py                # Script para detectar fogo em tempo real via webcam
│── requirements.txt         # Lista de dependências necessárias
│── fire.yaml                # Configuração do dataset para YOLO
```

## 🎯 Como Configurar o Ambiente

Para garantir um ambiente isolado e evitar conflitos entre bibliotecas, recomenda-se o uso de um ambiente virtual.

### Criando o ambiente virtual:
```bash
python -m venv venv
```

### Ativando o ambiente virtual:
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### Instalando as dependências:
```bash
pip install -r requirements.txt
```

## 🔥 Treinando o Modelo
Para treinar o modelo, execute:
```bash
python train.py
```

## 🎥 Detectando Fogo em Tempo Real
Após o treinamento, use o modelo para detectar fogo com a webcam:
```bash
python detect.py
```

Certifique-se de que o arquivo `best.pt` gerado durante o treinamento está no caminho correto (`runs/detect/train/weights/best.pt`).

## 📌 Observações
- Se necessário, ajuste os hiperparâmetros no `train.py` para melhorar a acurácia do modelo.
- Para utilizar outro conjunto de dados, edite o arquivo `fire.yaml` com os caminhos corretos.

🚀 **Agora você está pronto para detectar fogo em tempo real!** Se encontrar problemas ou melhorias, contribua com o projeto. 😃


 
