# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

Aram Paparian
Corpus: city_guides
---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

     This repo implements a retrieval augmented generation system (RAG) for the city_guides corpus. Users can ask the LLM questions regarding the locations mentioned throughout its various guides.
     
     The chunker splits the documents into chunks based on sections, rather than length. A relevance gate refuses answers to questions not contained in the corpus.
     
     An answer is generated using only the information contained within the corpus.

## Chunking Strategy

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->
     
     I didn't use a traditional size and overlap for the chunker. Rather, I split the chunks by section headers. This corpus was consistently labeled by section headers using a shared punctuation marker. Chunks split by section insured a full and singular thought aligned with each chunk.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

======================================================================
Chunk 2  |  source: guide_corry_vale.md#6  |  produced by: chunker.py::split_documents
======================================================================
Corry Vale
When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.

======================================================================
Chunk 3  |  source: guide_givens_mill.md#3  |  produced by: chunker.py::split_documents
======================================================================
Givens Mill
Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.

======================================================================
Chunk 4  |  source: guide_kestrelford.md#6  |  produced by: chunker.py::split_documents
======================================================================
Kestrelford
When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.

======================================================================
Chunk 5  |  source: guide_regional_transport.md#1  |  produced by: chunker.py::split_documents
======================================================================
Getting around the region
The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"How long does the train from Brightwater take to reach the regional hub?"

**Answer:**
The train from Brightwater takes 50 minutes to reach the regional hub.
Sources retrieved: guide_brightwater.md, guide_marchwood.md, guide_regional_transport.md, guide_thornby_wells.md

**My relevance cutoff:**
0.6. My sample data provided a wide range of .379 to .767 between accepted and refused answers. This allowed for quite a bit flexibity in determining the cutoff value. I stayed with the default.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| How long does the train from Brightwater take to reach the regional hub? | Yes | 0.236 |
| What seasons are recommended for visiting Kestrelford? | Yes | 0.274 |
| Which street in Brightwater is known for cheaper food options? | Yes | 0.298 |
| When is the best time to visit Corry Vale? | Yes | 0.311 |
| What day is the tearoom in Givens Mill closed? | Yes | 0.379 |

| What is the capital of Mongolia? | No | 0.767 |
| How do I change the oil in a diesel engine? | No | 0.880 |
| Who won the 1994 World Cup? | No | 0.908 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.841 |
| How do I write a for loop in Rust? | No | 0.859 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I asked Copilot for help in implemented the chunking function. I prescribed the strategy, after noticing that the corpus was neatly organized by sections that followed a consistent punctuation style. AI returned the ordering of ".strip" and ".split" following the default function as a template.

**2.**
I asked Copilot to aid in determining the relevance cutoff. My in scope and out of scope questions were neatly grouped below .38 or above .76, respectively. Copilot suggested I remain with the default provided value of 0.6, since any value within the range would be considered appropriate.

**
In addition, the conversational memory stretch feature was implemented near its entirety by Claude Code.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->
Metadata filtering — let people narrow results by source or date. (only by source)
Conversational memory — let the next question build on the last one. (ask questions until you quit)
---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. No chunk is under 40 characters or over 600 | 5 of 5 | 4/5 | 4/5 | 4/5 | MISSED |
| 5. Every answer comes back in under 30 seconds | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
1. Retrieved chunk contains the answer
Produced by: run_eval.py::main and store.py::search and scorer.py::judge

Output:
| How long does the train from Brightwater take to reach the regional hub? | pass | pass | pass |
- The train from Brightwater takes 50 minutes to reach the regional hub

| What seasons are recommended for visiting Kestrelford? | pass | pass | pass |
- Late spring and early autumn are recommended for visiting Kestrelford

| Which street in Brightwater is known for cheaper food options? | pass | pass | pass |
- Corry Lane is the street known for cheaper food options in Brightwater, where the food costs about a third less than on the riverside strip

| When is the best time to visit Corry Vale? | pass | pass | pass |
- The best time to visit Corry Vale is from May to September. Outside of these months, amenities close earlier, footpaths become very boggy, and the road above the second village is impassable in snow

| What day is the tearoom in Givens Mill closed? | pass | pass | pass |
- The tearoom is closed on Tuesdays


2. Every answer names a source
Produced by: run_eval.py::main and generate.py::answer_from_chunks

Output:
`guide_brightwater.md` (and also mentioned in `guide_regional_transport.md`).
`guide_kestrelford.md`
*guide_brightwater.md* and *guide_eating.md*
*guide_corry_vale.md*
guide_givens_mill.md

3. Gate stops out-of-corpus questions
Produced by: run_eval.py::check_out_of_scope and gate.py::check

Output:
| What is the capital of Mongolia? | 0.767 | refused |
| How do I change the oil in a diesel engine? | 0.880 | refused |
| Who won the 1994 World Cup? | 0.906 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.841 | refused |
| How do I write a for loop in Rust? | 0.859 | refused |

4. No chunk is under 40 characters or over 600
Produced by: run_eval.py::chunk_stats and chunker.py::split_documents

- Chunk length: 296-507 chars (1831 total)
- Chunk length: 210-464 chars (1617 total)
- Chunk length: 272-659 chars (1950 total)
- Chunk length: 225-300 chars (1359 total)
- Chunk length: 186-275 chars (1185 total)

5. Every answer comes back in under 30 seconds
Produced by: run_eval.py::timed_call

Output:
- Answer time: 1.39s
- Answer time: 0.53s
- Answer time: 0.63s
- Answer time: 0.64s
- Answer time: 0.50s
``

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer  | MET | All five questions passed in each run. The scorer checks the answer first, then defaults to checking the chunks retrieved |
| 2 | Every answer names a source | MET | Every response generates both the source the answer is drawn from at the end as reference, and a "sources retrieved" line |
| 3 | Gate stops out-of-corpus questions | MET | The relevance gate stops each out-of-corpus question, marked with 'refused' by the evaluator if it did not pass |
| 4 | No chunk is under 40 characters or over 600 | MISSED | One retreived result surpassed 600. The metric called for a perfect score, not a majority. |
| 5 | Every answer comes back in under 30 seconds | MET | The evaluator runs a timer that recorded the response time under 6 seconds for each run |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

     One retrieved chunk exceeded the 600 character target. Chunking is the stage that fails. The strategy never accounted for length, but the metric did, meaning the two were always out of sync. Section dividers could be missed if there is a typo or style change. The current check is rather rudimentary. Some sections, as shown by retieval, exceeded the range to begin with. The metric could be updated to account for what we know the corpus provides (lower bound 20, upper bound 800), but a length check in chunker would be more robust.

## The Improvement

**What I changed:**
I improved the chunking strategy to further split by paragraph. Chunks overlap by 1 paragraph where possible in order to avoid degrading the quality of responses by losing breadth of context, and inadvertantly fail citerion 1 as a side effect.

**Why I picked it:**
I chose this improvement because the metric related to chunking was the only one to fail. Previous evaluation had already flagged the chunking strategy for its potential to fall short

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. No chunk is under 40 characters or over 600 | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Every answer comes back in under 30 seconds | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

4. No chunk is under 40 characters or over 600
Produced by: run_eval.py::chunk_stats and chunker.py::split_documents

- Chunk length: 310-510 chars (2048 total)
- Chunk length: 213-467 chars (1752 total)
- Chunk length: 275-506 chars (1809 total)
- Chunk length: 228-425 chars (1513 total)
- Chunk length: 189-482 chars (1445 total)


**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->
     Yes, the metric is now fulfilled. The longest chunk retreived during evaluation was 659 characters. The index command had provided output of chunks exceeding 750 characters as well. Chunks now stay under the 600 character metric both during evaluation and the initial output provided when the corpus is indexed. Criterion 4 is now met, without impacting the success rate of the other criteria.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->
     Although the criterion is now met by the evaluators, there are still chunks created by the corpus that fall under 40. These chunks may be unlikely to surface for lacking breadth of information, but the potential still exists. I did not work on addressing the minimum because in order to stay focused on passing the criterion. I anticipated it to be an additional fix, merging sections, rather than splitting by paragraph.

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
     The timer based test was a nice addition because it required additional code to be written to support testing, but it was too easy. It's unlikely the tools we're using would exceed 30 seconds, and I'm not sure the code we're writing can have an impact one way or the other if the limit was set lower.

     The chunker could still use work to meet its lower bound, but maybe there doesn't need to be a minimum at all.
     
     I wonder if the section based splitting made criteria 1 too easy. A singular idea may be guaranteed when the corpus is neatly organized under a sub header.

## How I Used AI

     I relied on AI to quickly develop run_eval.py to be able to create output that measures criteria 4 and 5. This was additional print out for the range of lengths returned by each retrieval and a timer that recorded how long each response took