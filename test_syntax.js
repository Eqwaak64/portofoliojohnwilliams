const fs = require('fs');

const content = fs.readFileSync('d:/alanmenken/work.html', 'utf8');
const scriptMatches = content.match(/<script>(.*?)<\/script>/gs);

if (scriptMatches) {
    scriptMatches.forEach((script, idx) => {
        const code = script.replace(/<\/?script>/g, '');
        try {
            new Function(code);
            console.log(`Script ${idx} syntax OK`);
        } catch (e) {
            console.error(`Script ${idx} syntax ERROR:`, e);
        }
    });
} else {
    console.log("No scripts found");
}
