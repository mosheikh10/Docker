# What are Containers?

Containers package an application and its dependencies (bins/libs) into a single, isolated unit that runs consistently across environments.

- **Docker Container 1** → Runs App A + its own bins/libs  
- **Docker Container 2** → Runs App B + its own bins/libs  
- **Docker Container 3** → Runs App C + its own bins/libs  

All containers share the same:

- **Docker Engine** → Manages container lifecycle (start, stop, build, etc.)
- **Host Operating System** → Underlying OS that runs the Docker Engine
- **Infrastructure** → Hardware or cloud resources powering the host

✅ Benefit: Each app runs in isolation — no conflicts, easy to deploy, scale, or move anywhere.

# Containers Share the Host Kernel — And That’s a Good Thing

- **No separate OS per container** → Unlike virtual machines, containers don’t run their own OS. Instead, they share the host machine’s kernel.

- **Lightweight & fast** → Since they skip booting an OS, containers start in milliseconds and use far less memory/CPU.

- **Efficient resource use** → Multiple containers can run on the same host without heavy overhead — ideal for microservices and scaling.

- **Consistent behavior** → Apps run the same way whether on your laptop, staging, or production — because they’re bundled with everything they need (except the kernel).

- **Security boundary** → The kernel isolates containers via namespaces and cgroups — so one container can’t easily interfere with another or the host.

✅ Benefit: You get isolation and portability like VMs, but with speed and efficiency closer to running apps directly on the host.
