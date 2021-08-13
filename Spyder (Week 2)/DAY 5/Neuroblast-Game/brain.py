from game_utils import display_text
import constants
# import pygame
import pygame
#
# Importing modules related to keras and other functions necessary for neural network
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import keras.backend as K
from math import fabs
#
 
class Brain:
    
    def __init__(self):
        self.trained = True
        self.brain_name = "AI: Fire Constantly"
        self.mapShots = {}
        self.mapHits = {}
        # These two variables will be used by our Neural Network Class
        self.train_at_end = False
        self.currentInputs = np.array([list((0,0,0,0))])
        #     
        
    # Should I fire right now?
    def fire_decision(self, player_variables):
        return True
    
    # Track a fired bullet for learning
    def add_shot(self, bullet, player_variables):
        self.mapShots[bullet] = player_variables
    
    # Track hit bullets
    def record_hit(self, bullet):
        self.mapHits[bullet] = 1
    
    # Tracked missed bullets
    def record_miss(self, bullet):
        self.mapHits[bullet] = 0
    
    # Basic Brain never learns
    def train(self):
        pass
    
    def draw(self, screen):
        # This code will put a black background on the right side of the screen for us to draw over
        surf = pygame.Surface((640,720))
        surf.fill((0,0,0))
        screen.blit(surf,(640,0))
        #
        
        display_text(self.brain_name, 960, 60, constants.WHITE, screen)
        
class StaticBrain(Brain):
    
    # Initialization updated to store variables about number of hits and misses
    def __init__(self):
        Brain.__init__(self)
        self.brain_name = "AI: Fire When Player Below"
        self.total_bullets = 0
        self.total_hits = 0
        self.total_misses = 0
    #
    
    # Our "training" will simply be counting the number of total shots, total hits, and total misses
    def train(self):
        self.total_bullets = len(self.mapShots)
        self.total_hits = sum(self.mapHits.values())
        self.total_misses = len(self.mapHits.values()) - self.total_hits
    #
    
    # "Drawing" the brain will just be showing counts of shots, hits, and misses
    def draw(self, screen):
        super().draw(screen)
        
        display_text("Total Bullets Fired: " + str(self.total_bullets), 960, 90, constants.WHITE, screen)
        display_text("Total Bullets Hit: " + str(self.total_hits), 960, 120, constants.WHITE, screen)
        display_text("Total Bullets Missed: " + str(self.total_misses), 960, 150, constants.WHITE, screen)
    #
        
    def fire_decision(self, player_variables):
        y_distance = player_variables[1]
        if (y_distance < 0):
            return True
        else:
            return False
        
class LearningBrain(Brain):
    
    def __init__(self):
        Brain.__init__(self)
        self.brain_name = "AI: Find Optimal Fire Position"
        self.trained = False
        self.fire_x_optimal = 0
        self.fire_y_optimal = 0
        self.max_distance_from_optimal = constants.learning_brain_acceptable_range
        self.total_bullets = 0
        self.total_hits = 0
        self.total_misses = 0
        
        self.all_x_hits = []
        self.all_y_hits = []
        
    def record_hit(self, bullet):
        Brain.record_hit(self, bullet)
        differences = self.mapShots[bullet]
        self.all_x_hits.append(differences[0])
        self.all_y_hits.append(differences[1])
        
    def train(self):
        self.total_bullets = len(self.mapShots)
        self.total_hits = sum(self.mapHits.values())
        self.total_misses = len(self.mapHits.values()) - self.total_hits
	
        if (len(self.all_x_hits) > 0):
            self.fire_x_optimal = sum(self.all_x_hits) / len(self.all_x_hits)
            self.fire_y_optimal = sum(self.all_y_hits) / len(self.all_y_hits)
            self.trained = True
            
    def fire_decision(self, player_variables):
        x_distance_from_average = abs(player_variables[0] - self.fire_x_optimal)
        y_distance_from_average = abs(player_variables[1] - self.fire_y_optimal)
        if (x_distance_from_average < self.max_distance_from_optimal):
            if (y_distance_from_average < self.max_distance_from_optimal):
                return True
        return False

    def draw(self, screen):
        super().draw(screen)
        
        display_text("Total Bullets Fired: " + str(self.total_bullets), 960, 90, constants.WHITE, screen)
        display_text("Total Bullets Hit: " + str(self.total_hits), 960, 120, constants.WHITE, screen)
        display_text("Total Bullets Missed: " + str(self.total_misses), 960, 150, constants.WHITE, screen)
        
        display_text("Optimal X Difference: " + str(format(self.fire_x_optimal, '.2g')), 960, 180, constants.WHITE, screen)
        display_text("Optimal Y Difference: " + str(format(self.fire_y_optimal, '.2g')), 960, 210, constants.WHITE, screen)
        display_text("Acceptable Range Constant: " + str(self.max_distance_from_optimal), 960, 240, constants.WHITE, screen)

class NeuralNetworkBrain(Brain):
    
    def __init__(self):
        Brain.__init__(self)
        self.brain_name = "AI: Neural Network"
        self.train_at_end = True
        # We will use this weights variable when we start to visualize the network
        self.weights = []
        self.keras = Sequential()
        
        # We add the layers to the neural network here
        # The first layer is the input layer, where we specify the number of nodes, the shape of our input (4 variables), and the activation method
        # The 'relu' activation method stands for Rectified Linear Unit. This determines whether or not the node will count as "active"
        # Using this method means the threshold will only go to a minimum of 0, so there is no negative activation
        self.keras.add(Dense(4, input_shape=(4,), activation='relu'))
        # This adds a hidden layer to our network to make the relationship between variables more complicated.
        self.keras.add(Dense(4, activation='relu'))
        # The final layer is our output layer. The 'Sigmoid' activation will keep the output value between 0 and 1
        self.keras.add(Dense(1, activation='sigmoid'))
        # Once the layers are set up, we compile the neural network so it can be used by training and firing decisions
        # The mean squared error loss method ensures a positive result that minimizes large mistakes.
        # The 'sgd' optimizer stands for Stochastic Gradient Descent. It has a special way of determining how fast the neural network will learn.
        # The 'accuracy' metrics does not alter the way the method is trained, but we'll use that later when we visualize our data
        self.keras.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
        
        # Now that the layers are set up, we set up initial weights for our visualization later
        for layer in self.keras.layers:
            self.weights.append(layer.get_weights()[0])
        #
        
    def train(self):
        # x is the inputs to our model
        # y is the outputs based on those inputs
        x = []
        y = []
        for k,v in self.mapShots.items():
            # v stands for a set of player variables
            # k stands for a bullet
            if k in self.mapHits:
                a = list(v)
                x.append(a)
                y.append(self.mapHits[k])
        
        # Fit the data to the model
        # When we train neural networks, we make multiple passes over the network. 'nb_epoch' stands for the number of times we go over the dataset to train it
        # Batch size stands for the number of sets of data you use for a pass. So the below example will do 150 passes of training, picking 10 sets of data each time
        # The larger the batch size, and the larger the number of epochs, the more accurate the model might be, but it might also take longer to train.
        self.keras.fit(np.array(x),np.array(y),nb_epoch=150,batch_size=10)
        # We print some output to the interpreter to determine how accurate it is
        scores = self.keras.evaluate(np.array(x), np.array(y))
        print("\n%s: %.2f%%" % (self.keras.metrics_names[1], scores[1]*100))
 
        # Cache trained weights for visualization
        # Element 0 is weights, 1 is biases
        for layer in self.keras.layers:
            self.weights.append(layer.get_weights()[0])
            
    def fire_decision(self, player_variables):
        difference_x = player_variables[0]
        difference_y = player_variables[1]
        difference_velx = player_variables[2]
        difference_vely = player_variables[3]
        # Inputs need to be put into a numpy array
        network_inputs = np.array([list((difference_x, difference_y, difference_velx, difference_vely))])
        self.currentInputs = network_inputs
        
        #The predict method will return an output based on our inputs
        keras_prediction = self.keras.predict(network_inputs)
        if (keras_prediction >= constants.neural_network_activation_minimum):
            return True
        else:
            return False
        
    def get_activations(self, model, model_inputs, print_shape_only=False, layer_name=None):
        activations = []
        inp = model.input
    
        model_multi_inputs_cond = True
        if not isinstance(inp, list):
            inp = [inp]
            model_multi_inputs_cond = False
    
        # Get all the outputs for all the layers
        outputs = [layer.output for layer in model.layers if
                   layer.name == layer_name or layer_name is None]
    
        # Get all the trained functions for determining outputs
        funcs = [K.function(inp + [K.learning_phase()], [out]) for out in outputs]
    
        if model_multi_inputs_cond:
            list_inputs = []
            list_inputs.extend(model_inputs)
            list_inputs.append(1.)
        else:
            list_inputs = [model_inputs, 1.]
    
        # Place the activations in a list, this will be used when visualizing the network
        layer_outputs = [func(list_inputs)[0] for func in funcs]
        for layer_activations in layer_outputs:
            activations.append(layer_activations)
        return activations
    
    def layer_left_margin(self, number_of_neurons):
        return (constants.network_left_margin + 
                constants.horizontal_distance_between_neurons * 
                (constants.number_of_neurons_in_widest_layer - number_of_neurons) / 2)
        
    def get_synapse_colour(self, weight):
        if weight > 0:
            return 0, 255, 0
        else:
            return 255, 0, 0
        
    def draw(self, screen):
        # Set up necessary data to be used
        model = self.keras
        model_inputs = self.currentInputs
        weights = self.weights
        
        # We create a couple surfaces to draw on, the nsurf will be used to draw the nodes, the surf will be used to draw lines
        surf = pygame.Surface((640,720))
        nsurf = pygame.Surface((640,720))
        nsurf.fill((255,0,255))
        nsurf.set_colorkey((255,0,255))
        
        # Get the data from the model based on our inputs
        graph = self.get_activations(model, model_inputs)
        y = constants.network_bottom_margin
        # For each layer of nodes
        for layer in range(len(graph)):
            # Align it to the middle of the screen
            x = self.layer_left_margin(len(graph[layer][0]))
            # Draw each node in the layer
            for node in range(len(graph[layer][0])):
                if (layer+1 != len(graph)):
                    # Draw all connections between the nodes
                    for synapse in range(len(weights[layer+1][node])):
                        lo = constants.network_left_offset
                        to = constants.network_top_offset
                        x2 = synapse * constants.horizontal_distance_between_neurons + self.layer_left_margin(len(graph[layer+1][0]))
                        y2 = y + constants.vertical_distance_between_layers
                        pygame.draw.line(surf,self.get_synapse_colour(weights[layer+1][node][synapse]),
                                         (int(x+lo), int(y+to)), (int(x2+lo), int(y2+to)),
                                         max(1,int(fabs(weights[layer+1][node][synapse]))))
                lo = constants.network_left_offset
                to = constants.network_top_offset
                pygame.draw.circle(nsurf,(180,180,200),(int(x+lo), int(y+to)),constants.neuron_radius)
                display_text(str(round(graph[layer][0][node], 2)), x + 2+lo, y+to, constants.BLACK, nsurf)
                # After drawing one node, move to the right to draw the next one
                x += constants.horizontal_distance_between_neurons
            # After drawing one layer, move down to draw the next layer
            y += constants.vertical_distance_between_layers
        screen.blit(surf,(640,0))
        screen.blit(nsurf,(640,0)) 
        #Finally, add the AI name to the screen
        display_text(self.brain_name, 960, 60, constants.WHITE, screen)