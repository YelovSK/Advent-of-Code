// Build AoC.Library in Release config
using AoC.Library.CLI;
using CommandLine;
using System.Reflection;
using SolveOptions = AoC.Library.CLI.SolveOptions;

Parser.Default.ParseArguments<SolveOptions, CreateOptions>(args)
    .WithParsed<SolveOptions>(options => Commands.RunDay(options, Assembly.GetExecutingAssembly()))
    .WithParsed<CreateOptions>(Commands.CreateDayFolder);
