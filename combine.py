import torch
from models.experimental import attempt_load

def print_tensor_sizes(model, model_name):
    print(f"\nTensor sizes for {model_name}:")
    for name, param in model.named_parameters():
        print(f"{name}: {param.size()}")

def update_model_architecture(original_model, drone_model):
    # Check if architectures match
    assert original_model.yaml == drone_model.yaml, "Model architectures do not match!"

    # Update the architecture of the original model
    for layer_original, layer_drone in zip(original_model.model, drone_model.model):
        # Example: Update the number of filters in the first convolutional layer
        layer_original.conv = torch.nn.Conv2d(
            in_channels=layer_drone.conv.in_channels,
            out_channels=layer_drone.conv.out_channels,
            kernel_size=layer_drone.conv.kernel_size,
            stride=layer_drone.conv.stride,
            padding=layer_drone.conv.padding,
        )

    return original_model

def main():
    # Load the original YOLOv5 model
    original_model = attempt_load("/Users/karsonyounger/yolov5/yolov5m.pt")

    # Load the YOLOv5 model trained with the additional class (drone)
    drone_model = attempt_load("/Users/karsonyounger/yolov5/runs/train/exp2/weights/best.pt")

# Print tensor sizes for each model
    print_tensor_sizes(original_model, "Original Model")
    print_tensor_sizes(drone_model, "Drone Model")
    
    # Update the architecture of the original model
    updated_model = update_model_architecture(original_model, drone_model)

    # Combine weights using averaging
    for param_original, param_drone in zip(updated_model.parameters(), drone_model.parameters()):
        param_original.data = (param_original.data + param_drone.data) / 2

    # Save the combined model weights
    torch.save(updated_model.state_dict(), "combined_yolov5_weights.pt")

if __name__ == "__main__":
    main()
