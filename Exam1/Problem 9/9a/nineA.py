import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import torch
from PIL import Image
from torchvision import transforms 

model = torch.hub.load('pytorch/vision:v0.10.0', 'alexnet', pretrained=True)
model.eval()

filename1 = "C:/Users/zarin/OneDrive/Desktop/CS6510/Prob 9/Image/one.jpg"
filename2 = "C:/Users/zarin/OneDrive/Desktop/CS6510/Prob 9/Image/two.jpg"
filename3 = "C:/Users/zarin/OneDrive/Desktop/CS6510/Prob 9/Image/three.jpg"
filename4 = "C:/Users/zarin/OneDrive/Desktop/CS6510/Prob 9/Image/four.jpg"
filename5 = "C:/Users/zarin/OneDrive/Desktop/CS6510/Prob 9/Image/five.jpg"

file = (filename1, filename2, filename3, filename4, filename5) 

for i in range(0,5): 
    img = mpimg.imread(file[i]) 
    imgplot = plt.imshow(img)
    plt.title(label=f'Image {i+1}') 
    plt.show() 

for i in range(0,5): 
    input_image = Image.open(file[i]) 
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)
    
    output = model(input_batch) 
    
    probabilities = torch.nn.functional.softmax(output[0], dim=0)

    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]
        
    # Show top 5 categories per image
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    print("\nImage",i+1,":") 
    for i in range(top5_prob.size(0)):
        print(categories[top5_catid[i]], top5_prob[i].item())
    
    
