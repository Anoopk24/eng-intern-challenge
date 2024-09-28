const { exec } = require('child_process');

describe('translator.js script', () => {
    it('should output correct answer to the console', (done) => {
        exec("node translator.js Abc 123 xYz", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("O.....O.O...OO...........O......O.O....OO..........OO..OOOO.OOOO..OOO");
            done(); // Call the done callback
        });
    });
});