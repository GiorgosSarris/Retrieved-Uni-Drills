'''from typing import Union

def square(x: Union[int, float]) -> Union[int, float]:
    """Returns the square of a number."""
    return x * x

#optional: παιρενει τυπο ή none και επιστρεφει αναλογα τι δωσεις
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    """Returns a greeting message."""
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, World!"
    
#Any
from typing import Any
def echo(value: Any) -> Any:
    """Returns the same value that was passed in."""
    return value

#Lambda functions (shortcut of a function)
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x * x, nums))
print(squared_nums)  # Output: [1, 4, 9, 16, 25]
'''
#graph
from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph

"""first example i delete it:
class AgentState(TypedDict):
    message: str

     
def greeting_node(state: AgentState) -> AgentState:
    state['message'] = "Hello! How can I assist you today?" + state["message"]
    return state

graph=StateGraph(AgentState)
graph.add_node("greeter", greeting_node)  
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app= graph.compile()
result = app.invoke({"message": " bob "})
result["message"]
"""
#multiple input nodes

class AgentState2(TypedDict):
    values: List[int]
    name: str
    result: str

def process(state: AgentState2) -> AgentState2:
    #it will handle multiple inputs
    state['result'] = f"Hello {state['name']}, the sum is {sum(state['values'])}"
    return state

graph2=StateGraph(AgentState2)
graph2.add_node("processor", process)
graph2.set_entry_point("processor")
graph2.set_finish_point("processor")
app2= graph2.compile()

from IPython.display import display, Image
display(Image(app2.get_graph().draw_mermaid_png()))