# modules/command_handler.py
import ast
import subprocess

class CommandExecutor:
    """Executes commands securely."""

    @staticmethod
    def execute_command(command: list) -> str:
        """
        Executes a shell command securely and returns the output.
        """
        try:
            result = subprocess.run(
                command, capture_output=True, text=True, check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Command failed: {e.stderr}"
        except Exception as e:
            return f"Error during command execution: {e}"

    @staticmethod
    def evaluate_expression(expression: str) -> str:
        """
        Safely evaluates a mathematical expression.

        Args:
            expression (str): The expression to evaluate.

        Returns:
            str: The result of the evaluation.
        """
        try:
            # Allow only safe expressions (no function calls, variables, etc.)
            parsed = ast.parse(expression, mode='eval')
            if not all(isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.operator)) for node in ast.walk(parsed)):
                return "Unsafe expression detected!"
            return str(eval(expression))
        except Exception as e:
            return f"Error evaluating expression: {e}"
