// Semaphore definition
class Semaphore {
  constructor(max) {
    this.max = max;
    this.current = 0;
    this.queue = [];
  }

  async #acquire() {
    if (this.current < this.max) {
      this.current++;
      return;
    }
    return new Promise(resolve => this.queue.push(resolve));
  }

  #release() {
    this.current--;
    if (this.queue.length > 0) {
      const resolve = this.queue.shift();
      this.current++;
      resolve();
    }
  }

  async run(task) {
    await this.#acquire();
    try {
      return await task();
    } finally {
      this.#release();
    }
  }
}

// Semaphore usage
const semaphore = new Semaphore(3);

const asyncTask = num => new Promise(resolve => {
  console.log(`Task ${num} started`);
  setTimeout(() => {
    console.log(`Task ${num} completed`);
    resolve();
  }, Math.random() * 5000);
});

const runTasks = async () => {
  const tasks = Array.from({ length: 10 }, (_, i) => () => semaphore.run(() => asyncTask(i + 1)));
  await Promise.all(tasks.map(task => task()));
  console.log('All tasks completed');
};

runTasks();