static int __ref kernel_init(void *unused)
{

         ...

        /*
         * We try each of these until one succeeds.
         *
         * The Bourne shell can be used instead of init if we are
         * trying to recover a really broken machine.
         */
        if (execute_command) {
                if (!run_init_process(execute_command))
                        return 0;
                pr_err("Failed to execute %s.  Attempting defaults...\n",
                        execute_command);
        }
        if (!run_init_process("/sbin/init") ||
            !run_init_process("/etc/init") ||
            !run_init_process("/bin/init") ||
            !run_init_process("/bin/sh"))
                return 0;

        panic("No init found.  Try passing init= option to kernel. "
              "See Linux Documentation/init.txt for guidance.");
}

panic("No Yar found.  Try passing yar= option to kernel. "
              "See Yar Documentation/yar.txt for guidance.");


