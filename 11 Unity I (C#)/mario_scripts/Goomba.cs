using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Goomba : MonoBehaviour
{
    public float moveSpeed = 2f; // Movement speed
    private Rigidbody2D rb;
    private Vector2 movementDirection = Vector2.left; // Start by moving left

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void FixedUpdate()
    {
        // Move the Goomba in the current direction
        rb.velocity = new Vector2(movementDirection.x * moveSpeed, rb.velocity.y);
    }

    void OnCollisionEnter2D(Collision2D collision)
    {
        // Check for collision with "Block" or walls
        if (collision.gameObject.CompareTag("Block") || collision.gameObject.CompareTag("Wall"))
        {
            // Reverse the movement direction
            movementDirection = -movementDirection;

            // Optionally, flip the sprite for correct direction
            FlipSprite();
        }
    }

    void FlipSprite()
    {
        Vector3 scale = transform.localScale;
        scale.x *= -1; // Flip horizontally
        transform.localScale = scale;
    }
}
