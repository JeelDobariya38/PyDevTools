function trimCodeElements(className) {
    // It selects all elements with a specific class name on the webpage.

    // For each selected element (which is assumed to contain code blocks), it performs the following actions:

    // a. It retrieves the text content of the element, which includes the code block with potentially uneven indentation.

    // b. It splits the code content into individual lines based on newline characters (\n). This results in an array where each element represents a line of code.

    // c. It calculates the minimum indentation level by examining each line within the code block (excluding the first and last lines). It finds the number of leading spaces for each non-empty line and keeps track of the smallest number of leading spaces.

    // d. It then processes each line in the code block, including the first line, and removes the minimum indentation from each line. This ensures that the code's indentation remains consistent while unnecessary leading spaces are removed.

    // e. Finally, it updates the text content of the element with the cleaned code.

    var elements = document.querySelectorAll("." + className);
    for (var i = 0; i < elements.length; i++) {
        var codeElement = elements[i];
        var codeContent = codeElement.textContent;
        
        // Split the code content into lines
        var codeLines = codeContent.split('\n');
        var minIndent = Number.MAX_SAFE_INTEGER;

        // Find the minimum indentation level
        for (var j = 1; j < codeLines.length; j++) {
            var line = codeLines[j];
            if (line.trim() !== "") {
                var leadingSpaces = line.length - line.trimLeft().length;
                minIndent = Math.min(minIndent, leadingSpaces);
            }
        }

        var cleanedCode = "";

        // Remove the minimum indentation from each line, including the first line
        for (var j = 1; j < codeLines.length; j++) {
            var line = codeLines[j];
            cleanedCode += line.slice(minIndent) + "\n";
        }

        codeElement.textContent = cleanedCode;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    trimCodeElements("trim-code");
});
