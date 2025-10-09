from inline_snapshot import snapshot

from mirascope.llm import (
    AssistantMessage,
    Text,
    Thought,
    UserMessage,
)

sync_snapshot = snapshot(
    {
        "response": {
            "provider": "anthropic",
            "model_id": "claude-sonnet-4-0",
            "params": {"thinking": False},
            "finish_reason": None,
            "messages": [
                UserMessage(
                    content=[
                        Text(
                            text="How many primes below 400 contain 79 as a substring? Answer ONLY with the number, not sharing which primes they are."
                        )
                    ]
                ),
                AssistantMessage(
                    content=[
                        Thought(
                            thought="""\
I need to find all prime numbers below 400 that contain "79" as a substring.

First, let me think about what numbers below 400 could contain "79" as a substring:
- Numbers of the form 79X where X is a digit (790-799, but these are above 400)
- Numbers of the form X79 where X is a digit (179, 279, 379)
- Numbers of the form X79Y where X and Y are digits (this would give us numbers like 1790, 2791, etc., but these are above 400)

Wait, let me be more systematic. Numbers below 400 that contain "79" as a substring:

Two-digit numbers: 79
Three-digit numbers: 179, 279, 379, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799

But wait, 790-799 are all above 400? No, they're below 800, so they're below 400? No wait, 790 is greater than 400. Let me double-check: 790 > 400, so none of the 79X numbers work.

So the candidates are:
- 79
- 179  \n\
- 279
- 379

Now I need to check which of these are prime.

79: Let me check if 79 is prime.
79 = ? \n\
√79 ≈ 8.9, so I need to check divisibility by primes up to 8: 2, 3, 5, 7

79 is odd, so not divisible by 2.
7 + 9 = 16, not divisible by 3.
79 doesn't end in 0 or 5, so not divisible by 5.
79 ÷ 7 = 11.28..., so not divisible by 7.

So 79 is prime.


I'll continue checking 179's primality by testing divisibility up to 13. I'll systematically check each prime factor, starting with 11. 179 ÷ 11 looks like it might require careful calculation to determine divisibility.

Continuing the divisibility test, I find 179 is not divisible by 11 or 13. After methodically checking all primes up to its square root, I can confidently conclude 179 is indeed a prime number.

For 279, I quickly spot it's not prime. The digit sum test reveals divisibility by 3, and a simple division confirms 279 can be factored as 3 × 93.

Approaching 379's primality check, I'll need to test divisibility by primes up to its square root, which is approximately 19.5. I'll start by noting it's odd and not divisible by 2, and its digit sum isn't divisible by 3. The next step involves checking divisibility by 7.

After carefully testing divisibility by 7, 11, 13, 17, and 19, I find no factors. Each division leaves a remainder, confirming 379 is prime. To be thorough, I double-check my calculations, verifying no integer division exists for these prime divisors.

I identify three primes below 400 containing "79": 79, 179, and 379. Now I'm systematically exploring potential substring configurations, starting with number lengths. So far, I've noted 79 as the only two-digit prime with this substring.

For three-digit numbers, I'm investigating possible "79" placements, focusing on numbers starting with 1, 2, or 3.

I check each candidate's primality: 179 and 379 are prime, while 279 is divisible by 3. This confirms my initial list and validates the count of 3 primes.\
"""
                        ),
                        Text(
                            text="""\
Looking at numbers below 400 that contain "79" as a substring:

Two-digit: 79
Three-digit: 179, 279, 379

Checking which are prime:
- 79: prime
- 179: prime  \n\
- 279: divisible by 3 (2+7+9=18), so not prime
- 379: prime

3\
"""
                        ),
                    ]
                ),
                UserMessage(
                    content=[
                        Text(
                            text="If you remember what the primes were, then share them, or say 'I don't remember.'"
                        )
                    ]
                ),
                AssistantMessage(
                    content=[Text(text="The primes I found were 79, 179, and 379.")]
                ),
            ],
            "format": None,
            "tools": [],
        },
        "logging": [],
    }
)
async_snapshot = snapshot(
    {
        "response": {
            "provider": "anthropic",
            "model_id": "claude-sonnet-4-0",
            "params": {"thinking": False},
            "finish_reason": None,
            "messages": [
                UserMessage(
                    content=[
                        Text(
                            text="How many primes below 400 contain 79 as a substring? Answer ONLY with the number, not sharing which primes they are."
                        )
                    ]
                ),
                AssistantMessage(
                    content=[
                        Thought(
                            thought="""\
I need to find all prime numbers below 400 that contain "79" as a substring.

First, let me think about what numbers below 400 could contain "79" as a substring:
- Numbers of the form 79X (where X is a digit): 790, 791, 792, 793, 794, 795, 796, 797, 798, 799
- Numbers of the form X79 (where X is a digit): 179, 279, 379
- The number 79 itself

Wait, let me be more systematic. Numbers below 400 that contain "79":
- 79
- 179
- 279
- 379
- 790, 791, 792, 793, 794, 795, 796, 797, 798, 799 (but these are all ≥ 400, so they don't count)

So the candidates are: 79, 179, 279, 379

Now I need to check which of these are prime:

79: Let me check if 79 is prime.
√79 ≈ 8.9, so I need to check divisibility by primes up to 8: 2, 3, 5, 7
- 79 is odd, so not divisible by 2
- 7+9 = 16, not divisible by 3
- Doesn't end in 0 or 5, so not divisible by 5  \n\
- 79 ÷ 7 = 11.28..., so not divisible by 7
So 79 is prime.

179: Let me check if 179 is prime.
√179 ≈ 13.4, so I need to check divisibility by primes up to 13: 2, 3, 5, 7, 11, 13
- 179 is odd, so not divisible by 2


- 1+7+9 = 17, not divisible by 3
- Doesn't end in 0 or 5, so not divisible by 5
- 179 ÷ 7 = 25.57..., so not divisible by 7
- 179 ÷ 11 = 16.27..., so not divisible by 11
- 179 ÷ 13 = 13.77..., so not divisible by 13
So 179 is prime.

279: I notice 279 can be decomposed into 200 + 79. This suggests I should investigate its factors carefully.

Checking divisibility reveals key insights:
- Odd number, ruling out division by 2
- Digital sum of 18 indicates divisibility by 3
- 279 ÷ 3 = 93, which further breaks down to 3 × 31
- Ultimately, 279 = 9 × 31

Therefore, 279 is not a prime number.

379: I'll systematically test divisibility, focusing on primes up to its square root of about 19.5.
- Odd number, eliminating 2
- Digital sum doesn't match 3's divisibility
- Not divisible by 5
- Fails division tests for 7, 11, 13, 17, and 19

Consequently, 379 emerges as a prime number.

The primes below 400 containing "79" are 79, 179, and 379 - totaling 3 primes.\
"""
                        ),
                        Text(text="3"),
                    ]
                ),
                UserMessage(
                    content=[
                        Text(
                            text="If you remember what the primes were, then share them, or say 'I don't remember.'"
                        )
                    ]
                ),
                AssistantMessage(
                    content=[Text(text="I remember them: 79, 179, and 379.")]
                ),
            ],
            "format": None,
            "tools": [],
        },
        "logging": [],
    }
)
stream_snapshot = snapshot(
    {
        "response": {
            "provider": "anthropic",
            "model_id": "claude-sonnet-4-0",
            "finish_reason": None,
            "messages": [
                UserMessage(
                    content=[
                        Text(
                            text="How many primes below 400 contain 79 as a substring? Answer ONLY with the number, not sharing which primes they are."
                        )
                    ]
                ),
                AssistantMessage(
                    content=[
                        Thought(
                            thought="""\
I need to find all prime numbers below 400 that contain "79" as a substring.

First, let me think about what numbers below 400 could contain "79" as a substring:
- Numbers of the form 79X (where X is a digit): 790, 791, 792, 793, 794, 795, 796, 797, 798, 799
- Numbers of the form X79 (where X is a digit): 179, 279, 379
- The number 79 itself

Wait, I need to be more systematic. Numbers below 400 that contain "79":
- 79
- 179
- 279
- 379
- Any 4-digit number starting with 79 would be ≥ 790, but we only care about numbers < 400, so no 4-digit numbers qualify.

Wait, let me reconsider. We're looking at numbers below 400, so we can have:
- 79 (2 digits)
- X79 where X is 1, 2, or 3 (3 digits): 179, 279, 379

That's it. We can't have 479 or higher because that would be ≥ 400.
We can't have 79X because the smallest would be 790 which is ≥ 400.

So the candidates are: 79, 179, 279, 379

Now I need to check which of these are prime:

79: Let me check if 79 is prime.
Factors to check: √79 ≈ 8.9, so I need to check divisibility by 2, 3, 5, 7.
79 is odd, so not divisible by 2.
7 + 9 = 16, not divisible by 3.
Doesn't end in 0 or 5, so not divisible by 5.
79 ÷ 7 = 11.28..., so not divisible by 7.


79 is indeed prime.

I'll continue checking 179's primality by testing divisibility by 11 and 13.
Not divisible by 11 or 13, confirming 179 is prime.

For 279, I quickly discover it's divisible by 3. Dividing 279 by 3 yields 93, proving 279 is not prime.

Examining 379, I'll need to check divisibility up to its square root of approximately 19.5, testing prime numbers 2, 3, 5, 7, 11, 13, 17, and 19.

After methodical division tests, 379 passes each check. No factors found, confirming 379 is prime.

The substring "79" appears in three primes: 79, 179, and 379, totaling 3 primes.\
"""
                        ),
                        Text(
                            text="""\
Looking at numbers below 400 that contain "79" as a substring:
- 79
- 179  \n\
- 279
- 379

Checking which are prime:
- 79: prime
- 179: prime  \n\
- 279: divisible by 3 (2+7+9=18), so not prime
- 379: prime

3\
"""
                        ),
                    ],
                    provider="anthropic",
                    model_id="claude-sonnet-4-0",
                ),
                UserMessage(
                    content=[
                        Text(
                            text="If you remember what the primes were, then share them, or say 'I don't remember.'"
                        )
                    ]
                ),
                AssistantMessage(
                    content=[Text(text="I remember them: 79, 179, and 379.")],
                    provider="anthropic",
                    model_id="claude-sonnet-4-0",
                ),
            ],
            "format": None,
            "tools": [],
            "n_chunks": 5,
        },
        "logging": [],
    }
)
async_stream_snapshot = snapshot(
    {
        "response": {
            "provider": "anthropic",
            "model_id": "claude-sonnet-4-0",
            "finish_reason": None,
            "messages": [
                UserMessage(
                    content=[
                        Text(
                            text="How many primes below 400 contain 79 as a substring? Answer ONLY with the number, not sharing which primes they are."
                        )
                    ]
                ),
                AssistantMessage(
                    content=[
                        Thought(
                            thought="""\
I need to find all prime numbers below 400 that contain "79" as a substring.

First, let me think about what numbers below 400 could contain "79" as a substring:
- Numbers of the form 79X (where X is a digit): 790, 791, 792, 793, 794, 795, 796, 797, 798, 799
- Numbers of the form X79 (where X is a digit): 179, 279, 379
- The number 79 itself

Wait, 790 and above are ≥ 400, so I only need to consider up to 399.

So the candidates are:
- 79
- 179, 279, 379
- Numbers starting with 79 that are less than 400: none (since 790 > 400)

Wait, let me be more systematic. Numbers below 400 that contain "79":
- 79
- 179
- 279
- 379

Now I need to check which of these are prime.

79: Let me check if 79 is prime.
√79 ≈ 8.9, so I need to check divisibility by primes up to 8: 2, 3, 5, 7
79 is odd, so not divisible by 2
79 = 7 + 9 = 16, 1 + 6 = 7, not divisible by 3
79 doesn't end in 0 or 5, so not divisible by 5
79 ÷ 7 = 11.28..., so not divisible by 7
So 79 is prime.

179: Let me check if 179 is prime.
√179 ≈ 13.4, so I need to check divisibility by primes up to 13: 2, 3, 5, 7, 11, 13


179 is odd, so not divisible by 2
1 + 7 + 9 = 17, 1 + 7 = 8, not divisible by 3
179 doesn't end in 0 or 5, so not divisible by 5
179 ÷ 7 = 25.57..., so not divisible by 7
179 ÷ 11 = 16.27..., so not divisible by 11
179 ÷ 13 = 13.77..., so not divisible by 13
So 179 is prime.

I'll systematically test 279 for primality by checking divisibility of small prime numbers.

The number fails the divisibility test for 3, as its digit sum is divisible by 3. Dividing by 3 yields 93, confirming 279 is composite.

For 379, I systematically check divisibility by primes up to its square root. After testing 2, 3, 5, 7, 11, 13, 17, and 19, no divisors are found. This indicates 379 is prime.

I then review potential related numbers containing "79", focusing on those below 400. The candidates include 79, 179, 279, and 379. Primality testing reveals 79, 179, and 379 are prime.

However, 279 breaks this pattern, being composite. This leaves three prime numbers with "79" as a substring under 400.\
"""
                        ),
                        Text(text="3"),
                    ],
                    provider="anthropic",
                    model_id="claude-sonnet-4-0",
                ),
                UserMessage(
                    content=[
                        Text(
                            text="If you remember what the primes were, then share them, or say 'I don't remember.'"
                        )
                    ]
                ),
                AssistantMessage(
                    content=[Text(text="I remember them: 79, 179, and 379.")],
                    provider="anthropic",
                    model_id="claude-sonnet-4-0",
                ),
            ],
            "format": None,
            "tools": [],
            "n_chunks": 5,
        },
        "logging": [],
    }
)
without_raw_content_snapshot = snapshot(
    {
        "response": {
            "provider": "anthropic",
            "model_id": "claude-sonnet-4-0",
            "params": {"thinking": False},
            "finish_reason": None,
            "messages": [
                UserMessage(
                    content=[
                        Text(
                            text="How many primes below 400 contain 79 as a substring? Answer ONLY with the number, not sharing which primes they are."
                        )
                    ]
                ),
                AssistantMessage(
                    content=[
                        Thought(
                            thought="""\
I need to find all primes below 400 that contain "79" as a substring.

First, let me think about what numbers below 400 could contain "79" as a substring:
- Numbers of the form 79X (where X is a digit): 790, 791, 792, 793, 794, 795, 796, 797, 798, 799
- Numbers of the form X79 (where X is a digit): 179, 279, 379
- Numbers of the form X79Y (where X and Y are digits): This would give us numbers with at least 4 digits, starting from 1790, which are all ≥ 1790 > 400, so none of these are relevant.

Wait, let me be more systematic. The numbers below 400 that contain "79" as a substring are:

Two-digit: 79
Three-digit: 179, 279, 379, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799

But wait, we're looking for numbers below 400, so 790, 791, 792, 793, 794, 795, 796, 797, 798, 799 are all ≥ 790 > 400, so they don't qualify.

So the candidates are: 79, 179, 279, 379

Now I need to check which of these are prime:

79: Let me check if 79 is prime.
Factors to check: 2, 3, 5, 7 (since √79 ≈ 8.9)
79 ÷ 2 = 39.5 (not divisible)
79 ÷ 3 = 26.33... (not divisible)
79 ÷ 5 = 15.8 (not divisible)


79 ÷ 7 = 11.28... (not divisible)
So 79 is prime.

I'll continue checking 179 for primality. I'll test divisibility by 11 and 13, the next potential factors. 179 ÷ 11 = 16.27... (not divisible), and 179 ÷ 13 = 13.76... (not divisible). This suggests 179 is also prime.

Moving to 279, I quickly find it's not prime. Dividing by 3 yields 93, which breaks down to 3 × 31, revealing its composite nature.

For 379, I'll systematically check divisibility. After testing 2, 3, 5, and 7 without success, I'm midway through checking 11's divisibility.

Continuing through 13, 17, and 19, I confirm no factors exist. This means 379 is indeed prime.

Scanning the primes below 400 containing "79", I identify three: 79, 179, and 379.

The total count is 3 such primes.\
"""
                        ),
                        Text(
                            text="""\
Looking at numbers below 400 that contain "79" as a substring:

Two-digit: 79
Three-digit: 179, 279, 379

Checking primality:
- 79: prime
- 179: prime  \n\
- 279 = 3 × 93, not prime
- 379: prime

3\
"""
                        ),
                    ]
                ),
                UserMessage(
                    content=[
                        Text(
                            text="If you remember what the primes were, then share them, or say 'I don't remember.'"
                        )
                    ]
                ),
                AssistantMessage(
                    content=[Text(text="The primes were 79, 179, and 379.")]
                ),
            ],
            "format": None,
            "tools": [],
        },
        "logging": [],
    }
)
