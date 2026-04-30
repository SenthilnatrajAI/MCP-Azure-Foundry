import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

def get_blob_service_client():
    
@app.mcp_tool()
@app.mcp_tool_property(arg_name="name", description="Name of the user")
@app.mcp_tool_property(arg_name="item", description="product item or order id")
@app.mcp_tool_property(arg_name="quantitiy", description="Quantitiy of the product item")

def mcp_trigger(context):
    return "Hello I am MCPTool!"