Finetune Llama 3.2 in 30 Lines of Python

Code demonstrates how to finetune the Llama 3.2 model using the [Unsloth] library, which makes the process easy and fast.

### Features

- Finetunes Llama 3.2 model using the Unsloth library
- Implements Low-Rank Adaptation (LoRA) for efficient finetuning
- Uses the FineTome-100k dataset for training
- Configurable for different model sizes (1B and 3B)

### Installation

```bash
git clone https://github.com/abhishekdodda/abhi-llm-apps.git
cd abhi-llm-apps/llm_finetuning
pip install -r requirements.txt
```

## Usage

1. Open the script in Google Colab or your preferred Python environment.

2. Run the script to start the finetuning process:

```bash
# Run the entire script
python finetune_llama3.2.py
```

3. The finetuned model will be saved in the "finetuned_model" directory.

## How it Works

1. **Model Loading**: The script loads the Llama 3.2 3B Instruct model using Unsloth's FastLanguageModel.

2. **LoRA Setup**: Low-Rank Adaptation is applied to specific layers of the model for efficient finetuning.

3. **Data Preparation**: The FineTome-100k dataset is loaded and preprocessed using a chat template.

4. **Training Configuration**: The script sets up the SFTTrainer with specific training arguments.

5. **Finetuning**: The model is finetuned on the prepared dataset.

6. **Model Saving**: The finetuned model is saved to disk.

## Configuration

You can modify the following parameters in the script:

- `model_name`: Change to "unsloth/Llama-3.1-1B-Instruct" for the 1B model
- `max_seq_length`: Adjust the maximum sequence length
- `r`: LoRA rank
- Training hyperparameters in `TrainingArguments`

## Customization

- To use a different dataset, replace the `load_dataset` function call with your desired dataset.
- Adjust the `target_modules` in the LoRA setup to finetune different layers of the model.
- Modify the chat template in `get_chat_template` if you're using a different conversational format.
