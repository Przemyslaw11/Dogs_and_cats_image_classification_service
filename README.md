# Dogs-and-cats-image-classification-model
Model was made as an exercise in the science club : AGH_RACING

## Model's basic documentation:
⚫ Dataset consists of 2400 photos of cats and dogs in csv format. Training set consists of 2000 photos (83,33%) and testing set consists of 400 photos (16,66%)

⚪ First part of this sequential model has 32 filters, each 3x3 size, what's more I used 'ReLU' as an activation function (an advantage to ReLU other than avoiding vanishing gradients problem is that it has much lower run time. max(0,a) runs much faster than any sigmoid function). 

⚫ After every Conv2D, the MaxPooling2D function was used to progressively reduce the spatial size of the representation to reduce the amount of parameters and computation in the network.

⚪ Second part uses Flatten() function because the complex multidimensional data needs to be flattened to get the single-dimensional data as output. 
The 64 neurons in the dense layer get their source of input data from all the other neurons of the previous layer of the network, all the connections are made very deeply. 

⚫ The last neuron in Dense() function uses sigmoid function. It was used on purpose in the contex of binary classification of the model.

⚪ Binary_crossentropy loss is great decision for this implementation because it is independent for each vector component (class), meaning that the loss computed for every CNN output vector component is not affected by other component values. In the context of binary classification in this model it is natural to use Binary crossentropy.

⚫ Model was trained by 15 epochs in 64 photos packages. The model predicts dogs(0) and cats(1) on the photos with accuracy around 70%

### Dataset is available under the following link:
- https://drive.google.com/drive/folders/1dZvL1gi5QLwOGrfdn9XEsi4EnXx535bD?usp=sharing

### Code with full documentation of the model was saved in Google Colab notebook and is available at the following link : 
- https://colab.research.google.com/drive/1dkcp01chamW9iL8soy3ZAfiU1toO1Gwd#scrollTo=BSKMFaho8fui
