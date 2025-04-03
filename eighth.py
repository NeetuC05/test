# Step 1: Import libraries
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 2: Define the Bayesian Network structure
# Create a Bayesian Network with three nodes and edges
model = BayesianNetwork([
    ('Rain', 'Sprinkler'),  # Rain influences Sprinkler
    ('Rain', 'Grass Wet'),   # Rain influences Grass Wet
    ('Sprinkler', 'Grass Wet')  # Sprinkler influences Grass Wet
])

# Step 3: Define Conditional Probability Distributions (CPDs)
# Probability of Rain (prior probability)
cpd_rain = TabularCPD(variable='Rain', variable_card=2, values=[[0.7], [0.3]])  # P(Rain)

# Probability of Sprinkler given Rain
cpd_sprinkler = TabularCPD(
    variable='Sprinkler', 
    variable_card=2,
    values=[[0.8, 0.2],  # P(Sprinkler=OFF | Rain=0), P(Sprinkler=OFF | Rain=1)
            [0.2, 0.8]], # P(Sprinkler=ON  | Rain=0), P(Sprinkler=ON  | Rain=1)
    evidence=['Rain'], 
    evidence_card=[2]
)

# Probability of Grass Wet given Sprinkler and Rain
cpd_grass_wet = TabularCPD(
    variable='Grass Wet', 
    variable_card=2,
    values=[
        [0.99, 0.9, 0.8, 0.0],  # P(Grass Wet=0 | Sprinkler, Rain)
        [0.01, 0.1, 0.2, 1.0]   # P(Grass Wet=1 | Sprinkler, Rain)
    ],
    evidence=['Sprinkler', 'Rain'], 
    evidence_card=[2, 2]
)

# Step 4: Add CPDs to the model
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_grass_wet)

# Verify if the model is valid
if model.check_model():
    print("The Bayesian Network is valid!\n")
else:
    print("The Bayesian Network is not valid.\n")

# Step 5: Perform Inference

# Create an inference object
inference = VariableElimination(model)

# Query 1: Probability of Grass being wet
result_grass_wet = inference.query(variables=['Grass Wet'])
print("Probability of Grass Wet: \n", result_grass_wet, "\n")

# Query 2: Probability of Rain given that the Grass is Wet
result_rain_given_grass_wet = inference.query(variables=['Rain'], evidence={'Grass Wet': 1})
print("Probability of Rain given Grass is Wet:\n", result_rain_given_grass_wet)
