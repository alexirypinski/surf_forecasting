class MLPModel1():
    
    
    def __init__(train_set, test_set, n_inputs):
        #network init
        self.net = torch.nn.Sequential(
            torch.nn.Linear(n_inputs, 6),
            torch.nn.ReLU(),
            torch.nn.Linear(6, 6),
            torch.nn.ReLU(),
            torch.nn.Linear(6, 6),
            torch.nn.ReLU(),
            torch.nn.Linear(6, 6),
            torch.nn.ReLU(),
            torch.nn.linear(6, 1)
        )
        #variable init
        for i in range(5):
            net[2*i].init.normal_(0, 0.1)
            
        #adding dropout   
        d1 = torch.nn.dropout(p = 0.2, inplace=True)
        d2 = torch.nn.dropout(p = 0.4, inplace=True)
        
        d1(net[0])
        for i in range(1, 5):
            d2(net[2*i])
        
        self.trainset = train_set
        self.testset = testset
        
        
    
    #note, worried about minibatch remainder issues with loss (last minibatch has significantly less loss)
    #TODO: draw a train and testing graph, add dropoutlayers 
    
    
    def train_test(dataset_train, dataset_test, batch_size, learning_rate num_epochs, loss):
        #training loop 
        dataloader_train = torch.utils.data.DataLoader(dataset_train, batch_size = batch_size)
        dataloader_test = torch.utils.data.DataLoader(dataset_test, batch_size = batch_size)
        length = len(dataloader_train)
        optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate, momentum = 0.9)
        epoch_losses = []
        net.train()
        for epoch in range(num_epochs):
            running_loss = 0.0
            for X, y in dataloader_train: 
                optimizer.zero_grad_()
                y_hat = net(X)
                loss = loss(y_hat, y)
                loss.backward()
                with torch.no_grad():
                    running_loss += loss.item()
                optimizer.step()
            epoch_losses.append(running_loss/len(data_loader))
    
        
        #test loop
        epoch_losses_test = []
        net.eval()
        with torch.no_grad():
            length = len(dataloader_test)
            for epoch in range(num_epochs):
                running_loss = 0.0
                for X, y in dataloader_test:
                    y_hat = net(X)
                    loss = loss(y_hat, y)
                    running_loss += loss.item()
                epoch_losses_test.append(running_loss/length)
        
        return epoch_losses, epoch_losses_test
    
    #TODO, save to models folder
    def save(path):
        return None
    
    #TODO, add a validation step
    def train_val_test(dataset):
        return None 
        
        
        

