using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using TMPro; // For TextMeshPro

public class Player : MonoBehaviour
{
    public float moveSpeed = 5f;

    //public TextMeshProUGUI collisionText; 

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        // Get horizontal input (-1 for left, 1 for right)
        float horizontalInput = Input.GetAxis("Horizontal");

        // Calculate movement vector
        Vector3 movement = new Vector3(horizontalInput, 0f, 0f) * moveSpeed * Time.deltaTime;

        // Move the sprite
        transform.position += movement;
    }

    /*
    void OnCollisionEnter2D(Collision2D collision)
    {
        //collisionText.text = "Collided with: " + collision.gameObject.name;
        // Print a message to the Console when a 2D collision occurs
        Debug.Log("Collided with: " + collision.gameObject.name);


    }
    */

    void OnCollisionEnter2D(Collision2D collision)
    {
        // Check if Mario collides with a Goomba
        if (collision.gameObject.CompareTag("Goomba"))
        {
            // Determine if Mario is above the Goomba (stomp)
            float marioHeight = transform.position.y;
            float goombaHeight = collision.transform.position.y;

            if (marioHeight > goombaHeight + 0.5f) // Adjust the offset as needed
            {
                Debug.Log("Mario stomps the Goomba!");
                Destroy(collision.gameObject); // Remove the Goomba
            }
            else
            {
                Debug.Log("Mario is hit by the Goomba!");
                // Trigger Mario's damage logic, e.g., lose a life
                HandleMarioDamage();
            }
        }
    }

    private void HandleMarioDamage()
    {
        // Placeholder for Mario taking damage
        Debug.Log("Mario takes damage!");
    }
}
