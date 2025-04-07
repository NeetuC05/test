import tensorflow as tf
import numpy as np

# Create an instance of MirroredStrategy
strategy = tf.distribute.MirroredStrategy()

def dataset():
    (x_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data()
    x_train,x_test=x_train/255,x_test/255
    return(x_train,y_train),(x_test,y_test)
(x_train,y_train),(x_test,y_test)= dataset()
#print(x_train)

# Now you can access num_replicas_in_sync
batchsize=128*strategy.num_replicas_in_sync
train_dataset = tf.data.Dataset.from_tensor_slices((x_train,y_train)).shuffle(25000).batch(batchsize)
test_dataset = tf.data.Dataset.from_tensor_slices((x_test,y_test)).batch(batchsize)

with strategy.scope():
    model=tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28)), # Use Flatten instead of Flattened
        tf.keras.layers.Dense(128,activation='relu'),
        tf.keras.layers.Dense(10,activation='softmax')
        ])
    model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(train_dataset,epochs=10,validation_data=test_dataset) # Change epoch to epochs
loss,accuracy=model.evaluate(test_dataset)
print(accuracy)



import tensorflow as tf
import numpy as np


strategy = tf.distribute.MirroredStrategy()

def dataset():
    (x_train,y_train),(x_test,y_test)=tf.keras.datasets.imdb.load_data(num_words=10000)
    x_train=tf.keras.preprocessing.sequence.pad_sequences(x_train,value=0,padding='post',maxlen=500)
    x_test=tf.keras.preprocessing.sequence.pad_sequences(x_test,value=0,padding='post',maxlen=500)

    return(x_train,y_train),(x_test,y_test)
(x_train,y_train),(x_test,y_test)= dataset()

batchsize=128*strategy.num_replicas_in_sync
train_dataset = tf.data.Dataset.from_tensor_slices((x_train,y_train)).shuffle(50000).batch(batchsize)
test_dataset = tf.data.Dataset.from_tensor_slices((x_test,y_test)).batch(batchsize)

with strategy.scope():
    model=tf.keras.models.Sequential([
       tf.keras.layers.Embedding(10000,128,input_length=500),
       tf.keras.layers.LSTM(64,return_sequences=True),
       tf.keras.layers.LSTM(32),
       tf.keras.layers.Dense(10,activation='relu'),
       tf.keras.layers.Dense(1,activation='sigmoid')
        ])
    model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(train_dataset,epochs=10,validation_data=test_dataset)
loss,accuracy=model.evaluate(test_dataset)
print(accuracy)



# scaling
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Define model
def simple_nn():
    return nn.Linear(10, 1)

# Dummy data
x = torch.randn(100, 10)
y = torch.randn(100, 1)

# Create dataset and dataloader
dataset = TensorDataset(x, y)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Choose device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize model
model = simple_nn().to(device)

# Wrap with DataParallel if using multiple GPUs
if torch.cuda.device_count() > 1:
    print(f"Using {torch.cuda.device_count()} GPUs with DataParallel")
    model = nn.DataParallel(model)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(8):
    for batch in dataloader:
        inputs, labels = batch
        inputs = inputs.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
