# blockspring.lab

> blockspring public lab

## BLOCKSPRING-RELATED ideas, thoughts and feedback

### Comparison to AWS Lambda

 * Blockspring is poised to become a user-friendly variant of the AWS Lambda service
 * http://aws.amazon.com/lambda/

### Blockspring function input as arbitrary JSON struct

It would be great if the blockspring web-gui could also allow input arguments in the form of arbitrarily-sized JSON structs

Currently, blockspring web-gui allows function input arguments in the form of:
   * scalar name-value pairs
   * file-input
   * spreadsheet-like-grid

More detail here:
   * https://api.blockspring.com/docs/inputs

### Blockspring function code and invocations as signed commit objects

It would be great if blockspring web-gui allowed signed commits for function invocations.

This would enable the ability to do authenticated audit trails, just like with a git repository.

Any time a function is run, the arguments passed into the function and the output resulting from those inputs could both be signed by a committer and kept in an auditable trail that is capable of accepting branches and tags, just like git.

This would enable teams to transmit non-static content to each other with a degree of confidence in the accuracy, validity and authenticity of the content.

### Blockspring piping 

With blockspring output as arbitrary JSON structs, and blockspring input as arbitrary JSON structs, it is possible to create blockspring functions whose intput and output can be "piped" or chained together.

```
Expect the output of every program to become the input to another, as yet unknown, program. Don't clutter output with extraneous information. Avoid stringently columnar or binary input formats. Don't insist on interactive input.

~ Doug McIlroy
```

