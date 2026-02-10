(explanation-how-snaps-work-transactional-updates)=
# Transactional updates

A transactional update is an install or refresh operation on a set of snaps that either succeeds for all the snaps, or, if even one snap encounters an error, fails for all the entire set. If the process fails, all affected snaps revert to their state before the process started, even snaps that successfully updated.

This can help when a set of snaps with specific revisions are tested to ensure they work together, and where behaviour could become unpredictable if a set isn't installed or updated at the same time. 

Transactional updates can also help when you know that one snap is dependent on a specific revision of another, or when you need multiple snaps to update at the same time. On the firmware for device running Ubuntu Core, for example, it can help to update both the kernel snap and the gadget snap at the same time. Transactional updates enable this.

A transactional update or installation can be instantiated from either the **snap** command, or from the [SnapD REST API](/reference/api/redoc-static).

## Transactional updates from the snap command

The **snap install** and **snap refresh** commands accept an additional `--transaction=` argument with either `all-snaps` to instantiate the process as a single transaction, or `per-snap`, which is the default, for a separate transaction per listed snap:

To install hello and hello-world snaps as a single transaction, for example, run the following command:

```bash
$ snap install hello hello-world --transaction=all-snaps
hello-world 6.4 from Canonical✓ installed
hello 2.10 from Canonical✓ installed
```

Currently, no change, log, or message is output to show if a set of snaps have been installed as a single transaction.

