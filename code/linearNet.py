class LinearNet():
    
    def __init__(train_set, test_set, shape):
        self.shape = shape
        self.w = torch.normal(0, 0.1, size = (4, 1), requires_grad = True)
        self.b = torch.zeros((1, 1), requires_grad = True)
        self.train_set = train_set
        self.test_set = test_set

    def update_params_by_grad(params, learning_rate, batch_size):
        with torch.no_grad():
            for param in params:
                param -= param.grad * learning_rate / batch_size
        for param in params:
            param.grad.zero_()


    def model(X, w, b):
        return torch.matmul(X, w) + b

    #trains the model using SGD and graphs out and outputs running losses 
    def train_SGD(dataset, batch_size, learning_rate, num_epochs):  
        data_loader = torch.utils.data.DataLoader(dataset, batch_size = batch_size)
        epoch_losses = []
        for epoch in num_epochs:
            running_loss = 0.0
            for i, data in enumerate(data_loader):  
                X, y = data
                pred = model(X, w, b)
                y = y.reshape(pred.shape)
                l_vec = (pred - y)**2
                l = l_vec.sum()
                l.backwards()
                update_params_by_grad([w, b], learning_rate, batch_size)
                running_loss += l.item()
                
                if (i % len(data_loader)) == (len(data_loader) - 1):
                    epoch_losses.append(running_loss/len(data_loader))
                    
        plt.plot(list(range(1, num_epochs + 1)), epoch_losses)
        plt.ylabel("loss")
        plt.xlabel("epoch")
        plt.show()
        plt.savefig()
        

        
        return epoch_losses
                
                
                
                
    
    def test(): 
        return None

